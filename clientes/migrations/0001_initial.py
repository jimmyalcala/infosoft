# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Categoria'
        db.create_table(u'clientes_categoria', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'clientes', ['Categoria'])

        # Adding model 'Cliente'
        db.create_table(u'clientes_cliente', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('nombre', self.gf('django.db.models.fields.CharField')(max_length=200)),
            ('direccion', self.gf('django.db.models.fields.TextField')()),
            ('telefonos', self.gf('django.db.models.fields.CharField')(max_length=50)),
            ('ingreso', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modificado', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('geo', self.gf('django.db.models.fields.CharField')(max_length=50)),
        ))
        db.send_create_signal(u'clientes', ['Cliente'])

        # Adding M2M table for field categoria on 'Cliente'
        db.create_table(u'clientes_cliente_categoria', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('cliente', models.ForeignKey(orm[u'clientes.cliente'], null=False)),
            ('categoria', models.ForeignKey(orm[u'clientes.categoria'], null=False))
        ))
        db.create_unique(u'clientes_cliente_categoria', ['cliente_id', 'categoria_id'])


    def backwards(self, orm):
        # Deleting model 'Categoria'
        db.delete_table(u'clientes_categoria')

        # Deleting model 'Cliente'
        db.delete_table(u'clientes_cliente')

        # Removing M2M table for field categoria on 'Cliente'
        db.delete_table('clientes_cliente_categoria')


    models = {
        u'clientes.categoria': {
            'Meta': {'object_name': 'Categoria'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'clientes.cliente': {
            'Meta': {'object_name': 'Cliente'},
            'categoria': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['clientes.Categoria']", 'symmetrical': 'False'}),
            'direccion': ('django.db.models.fields.TextField', [], {}),
            'geo': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'ingreso': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'modificado': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'nombre': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'telefonos': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['clientes']