# Generated by Django 5.0.6 on 2024-06-22 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eventapp', '0002_alter_event_desc_alter_event_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='desc',
            field=models.CharField(max_length=500),
        ),
    ]
