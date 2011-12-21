# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'NewsPost'
        db.create_table('news_newspost', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('is_published', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('date_published', self.gf('django.db.models.fields.DateTimeField')(default=datetime.datetime.now)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('body', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('news', ['NewsPost'])

        # Adding M2M table for field related_shows on 'NewsPost'
        db.create_table('news_newspost_related_shows', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('newspost', models.ForeignKey(orm['news.newspost'], null=False)),
            ('show', models.ForeignKey(orm['radio.show'], null=False))
        ))
        db.create_unique('news_newspost_related_shows', ['newspost_id', 'show_id'])


    def backwards(self, orm):
        
        # Deleting model 'NewsPost'
        db.delete_table('news_newspost')

        # Removing M2M table for field related_shows on 'NewsPost'
        db.delete_table('news_newspost_related_shows')


    models = {
        'news.newspost': {
            'Meta': {'object_name': 'NewsPost'},
            'body': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'date_published': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_published': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'related_shows': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['radio.Show']", 'symmetrical': 'False', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
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
        }
    }

    complete_apps = ['news']
