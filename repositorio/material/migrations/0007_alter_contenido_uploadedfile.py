# Generated by Django 4.0.4 on 2022-06-25 19:42

from django.db import migrations, models
import material.models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0006_alter_contenido_uploadedfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='uploadedFile',
            field=models.FileField(blank=True, null=True, upload_to=material.models.user_directory_path),
        ),
    ]
