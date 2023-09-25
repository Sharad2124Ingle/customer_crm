from django.shortcuts import render, redirect
from .models import Offer
import secrets
import qrcode
from django.http import HttpResponse, HttpResponseServerError

from io import BytesIO
from urllib.parse import urlencode
from django.urls import reverse

def offer_list(request):
    offers = Offer.objects.all()
    return render(request, 'offer_list.html', {'offers': offers})


def redeem_offer(request, offer_id):
    #offer_id = request.session.get('selected_offer_id')
    offer = Offer.objects.get(pk=offer_id)
    if not offer.redeemed:
        offer.redeemed = True
        print(offer.qr_thread)
        
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
        qr.add_data(offer.qr_thread)
        qr.make(fit=True)

        response = HttpResponse(content_type="image/png")
        qr.make_image(fill_color="black", back_color="white").save(response, "PNG")
        offer.save()
        return response
        #return redirect('offer_confirmation')
    return redirect('offer_details')


def offer_details(request, offer_id):
    offer = Offer.objects.get(pk=offer_id)
    #request.session['selected_offer_id'] = offer_id
    return render(request, 'offer_details.html', {'offer': offer})

#in old logic it was kept as shop and only user will scann  and retail url will generate,
def generate_qr_code(request, offer_id):
    #offer_id = request.session.get('selected_offer_id')
    #request.session['selected_offer_id'] = offer_id
    qr_params = {'offer_id': offer_id}
    redeem_url = reverse('redeem_offer', args=[offer_id])
    qr_code_url = f"{request.build_absolute_uri(redeem_url)}?{urlencode(qr_params)}"

    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_code_url)
    qr.make(fit=True)
    
    # Create a BytesIO buffer to store the QR code image
    qr_code_buffer = BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(qr_code_buffer, "PNG")
    #del request.session['selected_offer_id']
    
    # Create the HTTP response with the QR code image
    response = HttpResponse(content_type="image/png")
    response.write(qr_code_buffer.getvalue())
    
    return response

"""    
def generate_shop_qr_code(request, offer_id):
    # You might want to include more information in the shop's QR code
    qr_data = f"Shop Redemption Data: Offer ID: {offer_id}"
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_data)
    qr.make(fit=True)
    
    qr_code_buffer = BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(qr_code_buffer, "PNG")
    
    response = HttpResponse(content_type="image/png")
    response.write(qr_code_buffer.getvalue())
    
    return response



#old logic
def redeem_offer(request):
    offer_id = request.session.get('selected_offer_id')
    offer = Offer.objects.get(pk=offer_id)
    if not offer.redeemed:
        offer.redeemed = True
        print(offer.qr_thread)
        #offer.save()
        qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )
        qr.add_data(offer.qr_thread)
        qr.make(fit=True)

        response = HttpResponse(content_type="image/png")
        qr.make_image(fill_color="black", back_color="white").save(response, "PNG")
        del request.session['selected_offer_id']
        return response
        #return redirect('offer_confirmation')
    return redirect('offer_details')

import qrcode
from io import BytesIO
from django.http import HttpResponse
from urllib.parse import urlencode
from django.urls import reverse

def generate_qr_code(request):
    offer_id = request.session.get('selected_offer_id')
    qr_params = {'offer_id': offer_id}
    redeem_url = reverse('redeem_offer')
    qr_code_url = f"{request.build_absolute_uri(redeem_url)}?{urlencode(qr_params)}"
    
    # Create a QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(qr_code_url)
    qr.make(fit=True)
    
    # Create a BytesIO buffer to store the QR code image
    qr_code_buffer = BytesIO()
    qr.make_image(fill_color="black", back_color="white").save(qr_code_buffer, "PNG")
    
    # Create the HTTP response with the QR code image
    response = HttpResponse(content_type="image/png")
    response.write(qr_code_buffer.getvalue())
    
    return response

def generate_confirmation_code(request, offer_id):
    
    # Generate a unique confirmation code
    confirmation_code = secrets.token_hex(4)
    request.session['confirmation_code'] = confirmation_code
    #confirmation_code = Offer.qr_thread
    #print(confirmation_code)
    return redirect('offer_confirmation')


def offer_confirmation(request):
    # Retrieve the confirmation code from the session
    confirmation_code = request.session.get('confirmation_code')
    scanned_code = request.session.get('confirmation_code')
    
    return render(request, 'offer_confirmation.html', {'confirmation_code': confirmation_code})
"""