from django.db import models

class Offer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    valid_until = models.DateField()
    qr_thread = models.CharField(max_length=100, default=None)
    redeemed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

 