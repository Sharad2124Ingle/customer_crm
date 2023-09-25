from django.shortcuts import render, redirect
from accounts.views import generate_totp_token

import requests
WHATSAPP_URL = 'https://graph.facebook.com/v17.0/121473941042143/messages'
WHATSAPP_TOKEN = 'Bearer EAARxbw6DhIYBO6vt097ttHgGg2tMhkMQpSzR3DreMX2RKUZC6cXTANNJUkJqyL40FoatXJ2ypzoGExjWbxKNW0tlCwjRSfQ0Kdyw9BgSc8YZC6TpE8tEuUDysRZBsMAHQWzhp8zO1QX5SAxwB44ZCsBp1crdHIpzmerBoh9xeHt2qoOJdAwTMX5Wg44LAFM8m2YBgS5ZB1VKD9W1YOGL17pPNd5QZD'

otp_token = generate_totp_token()


def mobiotp(request):
    if request.method == 'POST':
        
        motp(phone, msg)
        return redirect('otp_verification')
    
    return render(request, 'login_mobi_otp.html')



phone = "7798586194"
msg = "hi sharad"

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
    