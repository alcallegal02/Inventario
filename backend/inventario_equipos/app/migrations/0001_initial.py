# Generated by Django 5.1.3 on 2024-12-04 08:41

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Departamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Nave',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre_usuario', models.CharField(max_length=100, unique=True)),
                ('contraseña', models.CharField(max_length=128)),
                ('is_superuser', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Impresora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='impresoras', to='app.departamento')),
            ],
        ),
        migrations.AddField(
            model_name='departamento',
            name='nave',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='departamentos', to='app.nave'),
        ),
        migrations.CreateModel(
            name='Trabajador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellidos', models.CharField(max_length=100)),
                ('puesto_trabajo', models.CharField(max_length=100)),
                ('departamento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trabajadores', to='app.departamento')),
            ],
        ),
        migrations.CreateModel(
            name='Equipo',
            fields=[
                ('numero_serie', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=50)),
                ('marca', models.CharField(max_length=100)),
                ('modelo', models.CharField(max_length=100)),
                ('fecha_devolucion', models.DateField(blank=True, null=True)),
                ('ip', models.GenericIPAddressField(blank=True, null=True)),
                ('impresoras', models.ManyToManyField(blank=True, related_name='equipos', to='app.impresora')),
                ('trabajador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='equipos', to='app.trabajador')),
            ],
        ),
    ]
