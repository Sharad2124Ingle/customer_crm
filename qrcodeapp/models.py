import datetime
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from website.models import Record  # Import the Record model from website app
import os
from cryptography.fernet import Fernet


def generate_encryption_key():
    return Fernet.generate_key()

class QRCode(models.Model):
    record = models.ForeignKey(Record, on_delete=models.CASCADE)  # Use ForeignKey to associate QRCode with Record
    image = models.ImageField(upload_to='qr_codes/', blank=True, null=True)
    generated_at = models.DateTimeField()
    encryption_key = models.CharField(max_length=255, default='')
    expiration_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"QR Code for {self.record.first_name}"


