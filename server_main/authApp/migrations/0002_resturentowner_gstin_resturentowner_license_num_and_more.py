# Generated by Django 5.0.1 on 2024-02-16 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='resturentowner',
            name='gstin',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resturentowner',
            name='license_num',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='resturentowner',
            name='pan',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]