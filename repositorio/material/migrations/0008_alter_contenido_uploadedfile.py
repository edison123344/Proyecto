# Generated by Django 4.0.4 on 2022-06-25 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0007_alter_contenido_uploadedfile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contenido',
            name='uploadedFile',
            field=models.FileField(blank=True, null=True, upload_to='Contenido/'),
        ),
    ]
