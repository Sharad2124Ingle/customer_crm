from django.shortcuts import render, redirect
#from django.contrib.auth.forms import PasswordResetForm, PasswordResetConfirmForm
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.utils.http import urlsafe_base64_decode
from django.contrib import messages
from django.contrib.auth.forms import PasswordResetForm, SetPasswordForm
from django.core.mail import send_mail
from django_otp.decorators import otp_required
from website.models import Record
from django_otp import devices_for_user
from django.contrib.auth import authenticate
import pyotp
import base64
import os
from functools import wraps
from django.contrib.auth import login



User = get_user_model()

def forgot_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            # Save the form and get the user's email address
            user_email = form.save(request=request)
            # Send the password reset email
            send_mail(
                subject='Password Reset',
                message='Please click the link to reset your password.',
                from_email= 'sharadsingle@outlook.com',
                recipient_list=[user_email],
            )

            # Add success message and redirect to a confirmation page
            return render(request, 'password_reset_done.html')
    else:
        form = PasswordResetForm()

    return render(request, 'forgot_password.html', {'form': form})


def login_with_otp(request):
    if request.method == 'POST':
        username = request.POST.get('username')  # Can be email or username
        try:
            user = User.objects.get(username=username)  # Try to find the user by username
        except User.DoesNotExist:
            try:
                user = User.objects.get(email=username)  # Try to find the user by email
            except User.DoesNotExist:
                user = None
        
        if user:
            # Generate OTP token and send it via email
            otp_token = generate_totp_token()
            send_otp_email(user, otp_token)

            # Save the OTP token in the session
            request.session['otp_token'] = otp_token
            request.session['otp_user_id'] = user.pk

            # Redirect to the OTP verification page
            return redirect('otp_verification')
        else:
            messages.error(request, "Invalid credentials. Please try again.")

    return render(request, 'login_with_otp.html')


def generate_totp_token():
    # Generate a random secret key (bytes) to use as the base32-encoded secret
    random_bytes = os.urandom(20)

    # Base32-encode the random bytes to create the secret key
    secret_key = base64.b32encode(random_bytes).decode()

    # Create a TOTP object with the secret key
    totp = pyotp.TOTP(secret_key)

    # Generate the current TOTP token
    token = totp.now()
    return token


def send_otp_email(user, otp_token):
    # Send the OTP token via email
    send_mail(
        subject='OTP Verification',
        message=f'Your OTP for login is: {otp_token}',
        from_email='sharadsingle@outlook.com',
        recipient_list=[user.email],
    )


def otp_verification(request):
    if request.method == 'POST':
        otp = request.POST.get('otp')
        user_id = request.session.get('otp_user_id')
        otp_token = request.session.get('otp_token')

        if user_id and otp_token:
            try:
                user = User.objects.get(pk=user_id)
            except User.DoesNotExist:
                user = None

            if user:
                # Check if the entered OTP matches the generated OTP token
                if otp == otp_token:
                    # OTP verification successful, log in the user
                    login(request, user)
                    messages.success(request, "OTP verification successful. You are now logged in.")
                    return redirect('home')
                else:
                    messages.error(request, "Invalid OTP. Please try again.")
            else:
                messages.error(request, "User not found. Please try again.")
        else:
            messages.error(request, "OTP verification session not found. Please try again.")
    
    return render(request, 'otp_verification.html')


#How To Build WhatsApp Bulk Message Sender Using Python - (Extremely Usefull) | Free WhatsApp API
import requests
WHATSAPP_URL = 'https://graph.facebook.com/v17.0/121473941042143/messages'
WHATSAPP_TOKEN = 'Bearer EAARxbw6DhIYBOxxujx52KNzPF92LcvMhRjKLdxpeGEeGBZB7TZAOkEZCiZBMGSOVLVSinJSkLHk2Gb8AD1mEvDAAnaXYZBVkLrZCEgV9Rod3LZA7Y82pZATUHnZAZAfFAHmqPfEc3rXbXX4o06ZAQ98VZAzg6Nfpl4b9dZC0byrKO4ItXui3hpZAwBQ5xpoewQEazZBMkY0eDWmOqaoSBPinkp4ORXZCuQIKTWwZD'
"""
def mobileotp(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        phone = ('+91'+ phone)
        otp_token = generate_totp_token()
        msg = f'hi bhai: {otp_token}'
        motp(phone, msg)
        return redirect('otp_verification')
    
    return render(request, 'login_mobi_otp.html')

#phone = "+917798586194"
#msg = "hi sharaduman"
"""

def motp(phone, msg):
    headers = {"Authorization": WHATSAPP_TOKEN}
    payload = {
        "messaging_product": "whatsapp",
        "recipient_type": "individual",
        "to": phone,
        "type": "text",
        "text": {"body": msg}
    }
    response = requests.post(WHATSAPP_URL, headers=headers, json=payload)
    ans = response.json()
    return ans
    
from website.models import Record
def mobileotp(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')  # Can be email or username
        try:
            user = Record.objects.filter(phone=phone)  # Try to find the user by email
        except User.DoesNotExist:
            user = None
        
        if user:
            otp_token = generate_totp_token()
            phone = ('+91'+ phone)
            msg = f'your token: {otp_token}'
            motp(phone, msg)

            # Save the OTP token in the session
            request.session['otp_token'] = otp_token
            user = user.first()
            request.session['otp_user_id'] = user.pk

            # Redirect to the OTP verification page
            return redirect('otp_verification')
        else:
            messages.error(request, "Invalid credentials. Please try again.")

    return render(request, 'login_mobi_otp.html')

from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

"""
@csrf_exempt
def whatsapp_webhook(request):
    if request.method == 'GET':
        VERIFY_TOKEN = 'sharad_is_awesome'
        mode = request.GET['hub.mode']
        token =  request.GET['hub.verify_token']
        challenge = request.GET['hub.challenge']

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return HttpResponse(challenge, status = 200)
        else:
            return HttpResponse('error', ststus = 403)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        return HttpResponse('success', ststus=200)
""" 
@csrf_exempt
def whatsapp_webhook(request):
    if request.method == 'GET':
        VERIFY_TOKEN = 'sharad_is_awesome'
        
        # Check if the required query parameters are present
        if all(param in request.GET for param in ['hub.mode', 'hub.verify_token', 'hub.challenge']):
            mode = request.GET['hub.mode']
            token = request.GET['hub.verify_token']
            challenge = request.GET['hub.challenge']

            if mode == 'subscribe' and token == VERIFY_TOKEN:
                return HttpResponse(challenge, status=200)
            else:
                return HttpResponse('error', status=403)
        else:
            return HttpResponse('Missing parameters', status=400)
    
    if request.method == 'POST':
        data = json.loads(request.body)
        # Process the POST data here
        return HttpResponse('success', status=200)
