# Generated by Django 5.1.1 on 2024-09-18 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Tracking', '0005_alter_participant_participant_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='scfhs_number',
            field=models.CharField(max_length=50, null=True),
        ),
    ]