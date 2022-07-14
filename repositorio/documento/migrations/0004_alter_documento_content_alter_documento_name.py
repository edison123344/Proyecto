# Generated by Django 4.0.4 on 2022-07-14 01:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contenido', '0004_alter_contenido_material'),
        ('documento', '0003_rename_cintent_documento_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='content',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_posts', to='contenido.contenido', verbose_name='Contenido'),
        ),
        migrations.AlterField(
            model_name='documento',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Nombre del Documento'),
        ),
    ]
