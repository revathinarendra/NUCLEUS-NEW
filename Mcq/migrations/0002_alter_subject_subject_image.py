# Generated by Django 5.0.4 on 2024-04-11 06:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mcq', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subject',
            name='subject_image',
            field=models.ImageField(upload_to='subject_images/'),
        ),
    ]
