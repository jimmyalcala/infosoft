# -*- coding: utf-8 -*-
from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField('Nombre', max_length=50, unique=True)

    def __unicode__(self):
   		return self.nombre

class Pais(models.Model):
    nombre = models.CharField('Pais', max_length=50, unique=True)

    def __unicode__(self):
   		return self.nombre

class Estado(models.Model):
    nombre = models.CharField('Estado', max_length=50, unique=True)
    pais = models.ForeignKey(Pais)

    def __unicode__(self):
   		return self.nombre
   		

class Ciudad(models.Model):
    nombre = models.CharField('Ciudad', max_length=50, unique=True)
    estado = models.ForeignKey(Estado)

    def __unicode__(self):
   		return self.nombre
   		

    

class Cliente(models.Model):
	nombre = models.CharField('Nombre', max_length=200)
	direccion = models.TextField('Dirección')
	telefonos = models.CharField('Telefonos', max_length=50)
	ciudad = models.CharField('Ciudad', max_length=50)
	estado = models.CharField('Estado', max_length=50)
	ingreso = models.DateTimeField('Fecha de Ingreso', auto_now_add=True)
	modificado = models.DateTimeField('Fecha de Modificación',auto_now=True)
	geo = models.CharField('Geolocalización', max_length=50)
	categoria = models.ManyToManyField(Categoria)

	def __unicode__(self):
   		return self.nombre


	

