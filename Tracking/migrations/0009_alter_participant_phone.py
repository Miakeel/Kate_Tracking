# Generated by Django 5.1.1 on 2024-09-20 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracking', '0008_alter_participant_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='phone',
            field=models.IntegerField(blank=True),
        ),
    ]
