# Generated by Django 3.1.5 on 2022-06-12 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stp_api', '0002_auto_20210203_1748'),
    ]

    operations = [
        migrations.AddField(
            model_name='speechapimodel',
            name='vocab',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]