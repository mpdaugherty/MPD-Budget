# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'Budget'
        db.create_table('budgeting_budget', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('total', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
        ))
        db.send_create_signal('budgeting', ['Budget'])

        # Adding model 'Transaction'
        db.create_table('budgeting_transaction', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('budget', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['budgeting.Budget'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('amount', self.gf('django.db.models.fields.DecimalField')(max_digits=16, decimal_places=2)),
            ('note', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal('budgeting', ['Transaction'])


    def backwards(self, orm):
        
        # Deleting model 'Budget'
        db.delete_table('budgeting_budget')

        # Deleting model 'Transaction'
        db.delete_table('budgeting_transaction')


    models = {
        'budgeting.budget': {
            'Meta': {'object_name': 'Budget'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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
