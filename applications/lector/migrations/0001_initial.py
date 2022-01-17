# Generated by Django 4.0.1 on 2022-01-13 15:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('libro', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lector',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50, verbose_name='Nombres')),
                ('apellidos', models.CharField(max_length=50, verbose_name='Apellidos')),
                ('nacionalidad', models.CharField(max_length=20, verbose_name='Nacionalidad')),
                ('edad', models.PositiveIntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Prestamo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_prestamo', models.DateField(verbose_name='Fecha de prestamo')),
                ('fecha_devolucion', models.DateField(verbose_name='Fecha de devolución')),
                ('devuelto', models.BooleanField()),
                ('lector', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='lector.lector')),
                ('libro', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libro.libro')),
            ],
        ),
    ]
