# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'OrdenCompraWebpay.custom'
        db.add_column('webpay_ordencomprawebpay', 'custom',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=250, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'OrdenCompraWebpay.custom'
        db.delete_column('webpay_ordencomprawebpay', 'custom')


    models = {
        'webpay.ordencomprawebpay': {
            'Meta': {'object_name': 'OrdenCompraWebpay'},
            'codigo_autorizacion': ('django.db.models.fields.CharField', [], {'max_length': '8', 'blank': 'True'}),
            'codigo_transaccion': ('django.db.models.fields.CharField', [], {'max_length': '80', 'blank': 'True'}),
            'custom': ('django.db.models.fields.CharField', [], {'max_length': '250', 'blank': 'True'}),
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