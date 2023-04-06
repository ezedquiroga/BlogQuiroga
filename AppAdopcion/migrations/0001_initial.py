# Generated by Django 4.1.7 on 2023-04-06 01:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mascota',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('edad', models.CharField(max_length=8)),
                ('genero', models.CharField(max_length=6)),
                ('vacunas', models.CharField(max_length=20)),
                ('condicion_medica', models.CharField(max_length=20)),
                ('castrado_a', models.CharField(max_length=2)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='imagenes/')),
            ],
        ),
        migrations.CreateModel(
            name='Comentario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('mensaje', models.TextField(blank=True, null=True)),
                ('comentario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comentarios', to='AppAdopcion.mascota')),
            ],
        ),
    ]
