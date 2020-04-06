# Generated by Django 2.2 on 2020-04-06 13:10

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0008_auto_20200328_1150'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='is_verified',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='verification_uuid',
            field=models.UUIDField(default=uuid.uuid4, verbose_name='Unique Verification UUID'),
        ),
    ]
