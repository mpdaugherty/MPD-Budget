# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'Transaction.note'
        db.alter_column('budgeting_transaction', 'note', self.gf('django.db.models.fields.CharField')(max_length=300, null=True))


    def backwards(self, orm):
        
        # Changing field 'Transaction.note'
        db.alter_column('budgeting_transaction', 'note', self.gf('django.db.models.fields.TextField')(default='default note'))


    models = {
        'budgeting.budget': {
            'Meta': {'object_name': 'Budget'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '100'}),
            'total': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'})
        },
        'budgeting.transaction': {
            'Meta': {'object_name': 'Transaction'},
            'amount': ('django.db.models.fields.DecimalField', [], {'max_digits': '16', 'decimal_places': '2'}),
            'budget': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'transactions'", 'to': "orm['budgeting.Budget']"}),
            'date': ('django.db.models.fields.DateField', [], {'default': 'datetime.date.today'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.CharField', [], {'max_length': '300', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['budgeting']
