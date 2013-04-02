# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding unique constraint on 'Estado', fields ['nombre']
        db.create_unique(u'clientes_estado', ['nombre'])

        # Adding field 'Cliente.pais'
        db.add_column(u'clientes_cliente', 'pais',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['clientes.Pais']),
                      keep_default=False)


        # Renaming column for 'Cliente.ciudad' to match new field type.
        db.rename_column(u'clientes_cliente', 'ciudad', 'ciudad_id')
        # Changing field 'Cliente.ciudad'
        db.alter_column(u'clientes_cliente', 'ciudad_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Ciudad']))
        # Adding index on 'Cliente', fields ['ciudad']
        db.create_index(u'clientes_cliente', ['ciudad_id'])

        # Adding unique constraint on 'Cliente', fields ['nombre']
        db.create_unique(u'clientes_cliente', ['nombre'])


        # Renaming column for 'Cliente.estado' to match new field type.
        db.rename_column(u'clientes_cliente', 'estado', 'estado_id')
        # Changing field 'Cliente.estado'
        db.alter_column(u'clientes_cliente', 'estado_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Estado']))
        # Adding index on 'Cliente', fields ['estado']
        db.create_index(u'clientes_cliente', ['estado_id'])

        # Adding unique constraint on 'Ciudad', fields ['nombre']
        db.create_unique(u'clientes_ciudad', ['nombre'])

        # Adding unique constraint on 'Categoria', fields ['nombre']
        db.create_unique(u'clientes_categoria', ['nombre'])

        # Adding unique constraint on 'Pais', fields ['nombre']
        db.create_unique(u'clientes_pais', ['nombre'])


    def backwards(self, orm):
        # Removing unique constraint on 'Pais', fields ['nombre']
        db.delete_unique(u'clientes_pais', ['nombre'])

        # Removing unique constraint on 'Categoria', fields ['nombre']
        db.delete_unique(u'clientes_categoria', ['nombre'])

        # Removing unique constraint on 'Ciudad', fields ['nombre']
        db.delete_unique(u'clientes_ciudad', ['nombre'])

        # Removing index on 'Cliente', fields ['estado']
        db.delete_index(u'clientes_cliente', ['estado_id'])

        # Removing unique constraint on 'Cliente', fields ['nombre']
        db.delete_unique(u'clientes_cliente', ['nombre'])

        # Removing index on 'Cliente', fields ['ciudad']
        db.delete_index(u'clientes_cliente', ['ciudad_id'])

        # Removing unique constraint on 'Estado', fields ['nombre']
        db.delete_unique(u'clientes_estado', ['nombre'])

        # Deleting field 'Cliente.pais'
        db.delete_column(u'clientes_cliente', 'pais_id')


        # Renaming column for 'Cliente.ciudad' to match new field type.
        db.rename_column(u'clientes_cliente', 'ciudad_id', 'ciudad')
        # Changing field 'Cliente.ciudad'
        db.alter_column(u'clientes_cliente', 'ciudad', self.gf('django.db.models.fields.CharField')(max_length=50))

        # Renaming column for 'Cliente.estado' to match new field type.
        db.rename_column(u'clientes_cliente', 'estado_id', 'estado')
        # Changing field 'Cliente.estado'
        db.alter_column(u'clientes_cliente', 'estado', self.gf('django.db.models.fields.CharField')(max_length=50))

    models = {
        u'clientes.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'clientes.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Estado']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        },
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['clientes.Categoria']", 'symmetrical': 'False'}),
            'ciudad': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Ciudad']"}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Estado']"}),
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
            'Meta': {'object_name': 'Pais'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '50'})
        }
    }

    complete_apps = ['clientes']