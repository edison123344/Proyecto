# Generated by Django 4.0.4 on 2022-06-25 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('carrera', models.TextField(verbose_name='Carrera')),
                ('periodo', models.SmallIntegerField(default=0, verbose_name='Periodo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'carrera',
                'verbose_name_plural': 'carreras',
                'ordering': ['carrera'],
            },
        ),
        migrations.CreateModel(
            name='contenido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Nombre del Contenido')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'contenido',
                'verbose_name_plural': 'contenidos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='titulo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Titulo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
            ],
            options={
                'verbose_name': 'titulo',
                'verbose_name_plural': 'titulos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='temas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Nombre Tema')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Título')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('carrera', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.carrera', verbose_name='Carrera')),
            ],
            options={
                'verbose_name': 'titulo',
                'verbose_name_plural': 'titulos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(verbose_name='Nombre')),
                ('lastname', models.TextField(verbose_name='Apellido')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('titulo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.titulo', verbose_name='Titulo')),
            ],
            options={
                'verbose_name': 'titulo',
                'verbose_name_plural': 'titulos',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='material',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(verbose_name='Titulo')),
                ('descripcion', models.CharField(max_length=200, verbose_name='Descripcion')),
                ('image', models.ImageField(blank=True, null=True, upload_to='materia', verbose_name='Imagen')),
                ('silabo', models.CharField(max_length=200, verbose_name='Silabo')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Fecha de edición')),
                ('contenido', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.contenido', verbose_name='Contenido')),
                ('persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.persona', verbose_name='Carrera')),
                ('temas', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='material.temas', verbose_name='Tema')),
            ],
            options={
                'verbose_name': 'materia',
                'verbose_name_plural': 'materias',
                'ordering': ['title'],
            },
        ),
    ]
