# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'StationStatusUpdate'
        db.create_table('radio_stationstatusupdate', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_live', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('current_show', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['radio.Show'])),
            ('current_song', self.gf('django.db.models.fields.CharField')(max_length=255, blank=True)),
            ('timestamp', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
        ))
        db.send_create_signal('radio', ['StationStatusUpdate'])


    def backwards(self, orm):
        
        # Deleting model 'StationStatusUpdate'
        db.delete_table('radio_stationstatusupdate')


    models = {
        'radio.show': {
            'Meta': {'ordering': "('name',)", 'object_name': 'Show'},
            'detail_page_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'}),
            'full_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '255'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'short_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'}),
            'thumb_image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'null': 'True', 'blank': 'True'})
        },
        'radio.stationstatusupdate': {
            'Meta': {'ordering': "('-timestamp',)", 'object_name': 'StationStatusUpdate'},
            'current_show': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['radio.Show']"}),
            'current_song': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_live': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['radio']
