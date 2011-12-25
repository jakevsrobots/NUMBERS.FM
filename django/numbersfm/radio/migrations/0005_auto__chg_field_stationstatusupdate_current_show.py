# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Changing field 'StationStatusUpdate.current_show'
        db.alter_column('radio_stationstatusupdate', 'current_show_id', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['radio.Show'], null=True))


    def backwards(self, orm):
        
        # User chose to not deal with backwards NULL issues for 'StationStatusUpdate.current_show'
        raise RuntimeError("Cannot reverse this migration. 'StationStatusUpdate.current_show' and its values cannot be restored.")


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
            'current_show': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['radio.Show']", 'null': 'True', 'blank': 'True'}),
            'current_song': ('django.db.models.fields.CharField', [], {'max_length': '255', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_live': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'timestamp': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'})
        }
    }

    complete_apps = ['radio']
