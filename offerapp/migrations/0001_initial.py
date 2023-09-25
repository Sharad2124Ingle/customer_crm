# Generated by Django 4.2.3 on 2023-08-11 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('valid_until', models.DateField()),
                ('redeemed', models.BooleanField(default=False)),
            ],
        ),
    ]