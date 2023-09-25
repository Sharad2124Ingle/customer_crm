from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class RetailUser(AbstractUser):
    phone_no = models.CharField(max_length=15)
    shop_name = models.CharField(max_length=20)
    shop_id = models.CharField(max_length=10)
    mall_name = models.CharField(max_length=20)
    mall_id = models.CharField(max_length=10)
    address = models.CharField(max_length=30)
    city = models.CharField(max_length=10)
    state = models.CharField(max_length=10)
    zipcode = models.CharField(max_length=6)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)

    groups = models.ManyToManyField(
        Group,
        verbose_name=('Retail groups'),
        blank=True,
        help_text=('The groups this user belongs to.'),
        related_name='retailuser_set'  # Change this related_name
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name=('user permissions'),
        blank=True,
        help_text=('Specific permissions for this user.'),
        related_name='retailuser_set_user_permissions'  # Change this related_name
    )

    def __str__(self):
        return self.username
    # __str__ method and other fields/methods here
