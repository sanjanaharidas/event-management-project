# Generated by Django 5.0.6 on 2024-06-23 18:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0004_booking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='booked_on',
            new_name='Booked_on',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='booking_date',
            new_name='Booking_date',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='customer_name',
            new_name='Customer_name',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='customer_phone',
            new_name='Customer_phone',
        ),
        migrations.RenameField(
            model_name='booking',
            old_name='name',
            new_name='Event_name',
        ),
    ]
