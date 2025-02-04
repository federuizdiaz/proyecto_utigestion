# Generated by Django 5.1.4 on 2025-01-03 13:24

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfiles', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='link_web',
            field=models.URLField(blank=True, null=True, verbose_name='Enlace a una página web'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='descripcion',
            field=models.TextField(blank=True, null=True, verbose_name='Descripción'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Correo Electrónico'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='perfiles/', verbose_name='Imagen de Perfil'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='perfil', to=settings.AUTH_USER_MODEL, verbose_name='Usuario'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='Sitio Web'),
        ),
    ]
