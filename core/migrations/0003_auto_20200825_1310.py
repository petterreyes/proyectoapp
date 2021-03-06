# Generated by Django 3.0.8 on 2020-08-25 18:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200808_0944'),
    ]

    operations = [
        migrations.CreateModel(
            name='Docente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('email', models.EmailField(default='pettersf21115@hotmail.com', max_length=254)),
                ('sexo', models.CharField(max_length=1)),
                ('estado', models.IntegerField(default=1)),
                ('user', models.CharField(max_length=15)),
                ('usermod', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'docente',
                'verbose_name_plural': 'docente',
                'db_table': 'tr_docente',
                'ordering': ['created'],
            },
        ),
        migrations.CreateModel(
            name='Estudiante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=200)),
                ('apellido', models.CharField(max_length=200)),
                ('edad', models.IntegerField()),
                ('email', models.EmailField(default='pettersf21115@hotmail.com', max_length=254)),
                ('sexo', models.CharField(max_length=1)),
                ('estado', models.IntegerField(default=1)),
                ('user', models.CharField(max_length=15)),
                ('usermod', models.CharField(max_length=15)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'estudiante',
                'verbose_name_plural': 'estudiante',
                'db_table': 'tr_estudiante',
            },
        ),
        migrations.DeleteModel(
            name='Persona',
        ),
    ]
