# Generated by Django 2.2 on 2020-03-26 10:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0007_baseitem_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Educational',
            fields=[
                ('baseitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.BaseItem')),
                ('recommendede_ages', models.CharField(max_length=200)),
            ],
            bases=('content.baseitem',),
        ),
        migrations.AddField(
            model_name='baseitem',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='ItemsPic'),
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('educational_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.Educational')),
                ('author', models.CharField(max_length=200)),
                ('publisher', models.CharField(max_length=200)),
                ('language', models.CharField(choices=[('persian', 'persian'), ('english', 'englih')], max_length=50)),
            ],
            bases=('content.educational',),
        ),
        migrations.CreateModel(
            name='Stationery',
            fields=[
                ('educational_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='content.Educational')),
                ('color', models.CharField(max_length=100)),
                ('kind', models.CharField(choices=[('pen', 'pen'), ('pencil', 'pencil'), ('Ravan_nevis', 'Ravan_nevis')], max_length=50)),
                ('nib', models.CharField(choices=[('flat', 'flat'), ('ballbearings', 'ballbearings')], max_length=50)),
            ],
            bases=('content.educational',),
        ),
    ]