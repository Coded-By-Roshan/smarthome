# Generated by Django 3.2 on 2023-09-19 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='audiomodel',
            name='roomno',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='audiomodel',
            name='username',
            field=models.CharField(blank=True, default=0, max_length=100, null=True),
        ),
    ]