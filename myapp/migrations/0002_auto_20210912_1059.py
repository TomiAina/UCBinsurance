# Generated by Django 3.2.7 on 2021-09-12 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='Details',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='feature',
            name='Name',
            field=models.CharField(default='', max_length=100),
        ),
    ]
