from django.db import models

# Create your models here.
'''
class Project(models.Model):
    tittle = models.CharField(length=200)
    description = models.TextField()
    user = models.CharField(length=20)
    user_mod = models.CharField(length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Persona(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    email = models.EmailField()
    genero = models.CharField(max_length=2)
    estado = models.IntegerField()
    user = models.CharField(max_length=15)
    usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "persona"
        verbose_name = "persona"
        verbose_name_plural = "personas"
        ordering = ['created']

    def __str__(self):
        return self.apellido + ' ' + self.nombre

'''

class Docente(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    email = models.EmailField(default= "pettersf21115@hotmail.com")
    sexo = models.CharField(max_length=1)
    estado = models.IntegerField(default=1) #1 si esta activo y 2 si esta eliminado
    user = models.CharField(max_length=15)
    usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_docente"
        verbose_name = "docente"
        verbose_name_plural = "docente"
        ordering = ['created']

    def __str__(self):
        return self.apellido + ' ' + self.nombre


class Estudiante(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    email = models.EmailField(default= "pettersf21115@hotmail.com")
    sexo = models.CharField(max_length=1)
    estado = models.IntegerField(default=1) #1 si esta activo y 2 si esta eliminado
    user = models.CharField(max_length=15)
    usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_estudiante"
        verbose_name = "estudiante"
        verbose_name_plural = "estudiante"

    def __str__(self):
        return self.apellido

class Medicos(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    edad = models.IntegerField()
    email = models.EmailField()
    sexo = models.CharField(max_length=1)
    estado = models.IntegerField(default=1) #1 si esta activo y 2 si esta eliminado
    user = models.CharField(max_length=15)
    usermod = models.CharField(max_length=15)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = "tr_medicos"
        verbose_name = "medicos"
        verbose_name_plural = "medicos"

    def __str__(self):
        return self.apellido + ' ' + self.nombre

