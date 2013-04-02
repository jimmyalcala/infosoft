# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Estado'
        db.create_table(u'clientes_estado', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('pais', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Pais'])),
        ))
        db.send_create_signal(u'clientes', ['Estado'])

        # Adding model 'Ciudad'
        db.create_table(u'clientes_ciudad', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('estado', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['clientes.Estado'])),
        ))
        db.send_create_signal(u'clientes', ['Ciudad'])

        # Adding model 'Pais'
        db.create_table(u'clientes_pais', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'clientes', ['Pais'])

        # Adding field 'Cliente.ciudad'
        db.add_column(u'clientes_cliente', 'ciudad',
                      self.gf('django.db.models.fields.CharField')(default=2, max_length=50),
                      keep_default=False)

        # Adding field 'Cliente.estado'
        db.add_column(u'clientes_cliente', 'estado',
                      self.gf('django.db.models.fields.CharField')(default=datetime.datetime(2013, 4, 1, 0, 0), max_length=50),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Estado'
        db.delete_table(u'clientes_estado')

        # Deleting model 'Ciudad'
        db.delete_table(u'clientes_ciudad')

        # Deleting model 'Pais'
        db.delete_table(u'clientes_pais')

        # Deleting field 'Cliente.ciudad'
        db.delete_column(u'clientes_cliente', 'ciudad')

        # Deleting field 'Cliente.estado'
        db.delete_column(u'clientes_cliente', 'estado')


    models = {
        u'clientes.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'clientes.ciudad': {
            'Meta': {'object_name': 'Ciudad'},
            'estado': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Estado']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['clientes.Categoria']", 'symmetrical': 'False'}),
            'ciudad': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'estado': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'geo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingreso': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telefonos': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'clientes.estado': {
            'Meta': {'object_name': 'Estado'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'pais': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['clientes.Pais']"})
        },
        u'clientes.pais': {
            'Meta': {'object_name': 'Pais'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['clientes']