# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'OrdenCompraWebpay'
        db.create_table('webpay_ordencomprawebpay', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('orden_compra', self.gf('django.db.models.fields.CharField')(unique=True, max_length=42)),
            ('respuesta', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('monto', self.gf('django.db.models.fields.PositiveIntegerField')(default=0)),
            ('codigo_autorizacion', self.gf('django.db.models.fields.CharField')(max_length=8, blank=True)),
            ('final_num_tarjeta', self.gf('django.db.models.fields.CharField')(max_length=4, blank=True)),
            ('tipo_pago', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('fecha_transaccion', self.gf('django.db.models.fields.DateTimeField')(null=True, blank=True)),
            ('id_transaccion', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('status', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('codigo_transaccion', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('id_sesion', self.gf('django.db.models.fields.CharField')(max_length=80, blank=True)),
            ('tipo_transaccion', self.gf('django.db.models.fields.CharField')(max_length=30, blank=True)),
            ('fecha_contable', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('numero_cuota', self.gf('django.db.models.fields.CharField')(max_length=10, blank=True)),
        ))
        db.send_create_signal('webpay', ['OrdenCompraWebpay'])


    def backwards(self, orm):
        # Deleting model 'OrdenCompraWebpay'
        db.delete_table('webpay_ordencomprawebpay')


    models = {
        'webpay.ordencomprawebpay': {
            'Meta': {'object_name': 'OrdenCompraWebpay'},
            'codigo_autorizacion': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'codigo_transaccion': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'fecha_contable': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'fecha_transaccion': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
            'final_num_tarjeta': ('django.db.models.fields.CharField', [], {'max_length': '4', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'id_sesion': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'id_transaccion': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'monto': ('django.db.models.fields.PositiveIntegerField', [], {'default': '0'}),
            'numero_cuota': ('django.db.models.fields.CharField', [], {'max_length': '10', 'blank': 'True'}),
            'orden_compra': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '42'}),
            'respuesta': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'status': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'tipo_pago': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'tipo_transaccion': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'})
        }
    }

    complete_apps = ['webpay']