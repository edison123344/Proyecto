# Generated by Django 4.0.4 on 2022-07-07 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('material', '0016_alter_temascontenido_contenido'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='temascontenido',
            options={'ordering': ['name'], 'verbose_name': 'tipocontenido', 'verbose_name_plural': 'tiposcontenidos'},
        ),
        migrations.RemoveField(
            model_name='material',
            name='Contenido',
        ),
        migrations.RemoveField(
            model_name='temascontenido',
            name='Contenido',
        ),
        migrations.AddField(
            model_name='material',
            name='contenido',
            field=models.ManyToManyField(related_name='get_posts', to='material.temascontenido', verbose_name='Contenido'),
        ),
        migrations.AddField(
            model_name='temascontenido',
            name='contenido',
            field=models.ManyToManyField(blank=True, related_name='get_posts', to='material.contenido', verbose_name='Contenido'),
        ),
    ]
