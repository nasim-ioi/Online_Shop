# Generated by Django 2.2 on 2020-03-28 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20200328_0908'),
    ]

    operations = [
        migrations.AddField(
            model_name='baseitem',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]