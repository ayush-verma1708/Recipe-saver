# Generated by Django 4.2.3 on 2023-07-29 08:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='students',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=''),
        ),
    ]
