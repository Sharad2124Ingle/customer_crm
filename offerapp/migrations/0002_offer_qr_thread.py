# Generated by Django 4.2.3 on 2023-08-11 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('offerapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='offer',
            name='qr_thread',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
