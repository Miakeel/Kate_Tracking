# Generated by Django 5.1.1 on 2024-09-17 11:44

import phone_field.models
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracking', '0002_qrcodeid_entry'),
    ]

    operations = [
        migrations.AddField(
            model_name='participant',
            name='inside',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='participant',
            name='phone',
            field=phone_field.models.PhoneField(blank=True, max_length=31),
        ),
        migrations.AlterField(
            model_name='qrcodeid',
            name='id',
            field=models.UUIDField(blank=True, default=uuid.uuid4, primary_key=True, serialize=False, unique=True),
        ),
    ]
