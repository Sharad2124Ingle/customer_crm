from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
import qrcode
from io import BytesIO
from .models import QRCode  # Import the QRCode model from the 'qrcodeapp'
from django.http import HttpResponse
from datetime import datetime, timedelta
import os
from django.utils import timezone
from website.models import Record
from django.utils.timezone import make_aware, now, timedelta, utc
from django.conf import settings
from django.urls import reverse
import base64
from cryptography.fernet import Fernet
from .models import QRCode

from qrcode import make as make_qr_code
from PIL import Image
from django.template.loader import render_to_string

@login_required
def select_record(request):
    # Get the records for the current logged-in user
    records = Record.objects.filter(user=request.user)

    return render(request, 'select_record.html', {'records': records})

@login_required
def auto_refresh_view(request, record_id):
    # Get the URL for the 'generate_qr_code' view with the given record_id
    generate_qr_code_url = reverse('qrcodeapp:generate_qr_code', args=[record_id])
    
    # Redirect back to the 'generate_qr_code' page after a delay of 2 minutes (120 seconds)
    return redirect(generate_qr_code_url)



@login_required
def generate_qr_code(request, record_id):
    record = get_object_or_404(Record, pk=record_id)
    current_datetime = make_aware(datetime.now(), timezone=utc)

    qr_code_validity_duration = timedelta(minutes=2)
    
    try:
        qr_code = QRCode.objects.get(record=record)
        if qr_code.generated_at and (current_datetime - qr_code.generated_at) < qr_code_validity_duration:
            #return render(request, 'generate_qr_code.html', {'qr_code': record})
            with open(qr_code.image.path, 'rb') as img_file:
                #return render(request, 'generate_qr_code.html', {'qr_code': img_file})
                return HttpResponse(img_file.read(), content_type="image/png")
        else:
            qr_code.delete()
    except QRCode.DoesNotExist:
        pass
    
    qr_data = f"ID: {record.id}\nName: {record.first_name}\nMobile: {record.phone}\nVehicle No: {record.vehicle}\ntime: {current_datetime}"

    encryption_key = Fernet.generate_key()
    cipher_suite = Fernet(encryption_key)
    encrypted_data = cipher_suite.encrypt(qr_data.encode())

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=4,
        border=4,
    )
    qr.add_data(encrypted_data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    buffer = BytesIO()
    img.save(buffer)

    qr_code_directory = os.path.join(settings.MEDIA_ROOT, 'qr_codes')
    os.makedirs(qr_code_directory, exist_ok=True)

    qr_code_image_filename = f'qr_code_{record.id}.png'  # Use the record ID in the filename

    qr_code_image_path = os.path.join(qr_code_directory, qr_code_image_filename)

    with open(qr_code_image_path, 'wb') as img_file:
        img.save(img_file)

    qr_code = QRCode.objects.create(
        record=record,
        image=qr_code_image_path,
        generated_at=current_datetime,
        encryption_key=encryption_key
    )

    context = {
        'qr_code': qr_code,
        'timestamp': int(timezone.now().timestamp() * 1000),
    }
    return render(request, 'generate_qr_code.html', {'qr_code': record})






