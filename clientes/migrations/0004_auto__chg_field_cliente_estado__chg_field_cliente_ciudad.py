# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Cliente.estado'
        db.alter_column(u'clientes_cliente', 'estado_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['clientes.Estado']))

        # Changing field 'Cliente.ciudad'
        db.alter_column(u'clientes_cliente', 'ciudad_id', self.gf('smart_selects.db_fields.ChainedForeignKey')(to=orm['clientes.Ciudad']))

    def backwards(self, orm):

        # Changing field 'Cliente.estado'
        db.alter_column(u'clientes_cliente', 'estado_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Estado']))

        # Changing field 'Cliente.ciudad'
        db.alter_column(u'clientes_cliente', 'ciudad_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Ciudad']))

    models = {
        u'clientes.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'clientes.ciudad': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Ciudad'},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Estado']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['clientes.Categoria']", 'symmetrical': 'False'}),
            'ciudad': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['clientes.Ciudad']"}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'estado': ('smart_selects.db_fields.ChainedForeignKey', [], {'to': u"orm['clientes.Estado']"}),
            'geo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingreso': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '200'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Pais']"}),
            'telefonos': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'clientes.estado': {
            'Meta': {'object_name': 'Estado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Pais']"})
        },
        u'clientes.pais': {
            'Meta': {'ordering': "['nombre']", 'object_name': 'Pais'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['clientes']