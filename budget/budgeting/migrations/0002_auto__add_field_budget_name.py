# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Budget.name'
        db.add_column('budgeting_budget', 'name', self.gf('django.db.models.fields.CharField')(default='Default Budget Name', unique=True, max_length=100), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Budget.name'
        db.delete_column('budgeting_budget', 'name')


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
            'budget': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['budgeting.Budget']"}),
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'note': ('django.db.models.fields.TextField', [], {})
        }
    }

    complete_apps = ['budgeting']
