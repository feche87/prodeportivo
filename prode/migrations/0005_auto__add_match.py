# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Match'
        db.create_table(u'prode_match', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('first_team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='match_first_team', to=orm['prode.Team'])),
            ('second_team', self.gf('django.db.models.fields.related.ForeignKey')(related_name='match_second_team', to=orm['prode.Team'])),
            ('date', self.gf('django.db.models.fields.DateField')()),
            ('start_datetime', self.gf('django.db.models.fields.TimeField')()),
            ('first_team_goals', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
            ('second_team_goals', self.gf('django.db.models.fields.PositiveIntegerField')(null=True)),
        ))
        db.send_create_signal(u'prode', ['Match'])


    def backwards(self, orm):
        # Deleting model 'Match'
        db.delete_table(u'prode_match')


    models = {
        u'prode.company': {
            'Meta': {'object_name': 'Company'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'logo': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'prode.department': {
            'Meta': {'object_name': 'Department'},
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prode.Company']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'prode.match': {
            'Meta': {'object_name': 'Match'},
            'date': ('django.db.models.fields.DateField', [], {}),
            'first_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'match_first_team'", 'to': u"orm['prode.Team']"}),
            'first_team_goals': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'second_team': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'match_second_team'", 'to': u"orm['prode.Team']"}),
            'second_team_goals': ('django.db.models.fields.PositiveIntegerField', [], {'null': 'True'}),
            'start_datetime': ('django.db.models.fields.TimeField', [], {})
        },
        u'prode.phase': {
            'Meta': {'object_name': 'Phase'},
            'finish_date': ('django.db.models.fields.DateField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'}),
            'start_date': ('django.db.models.fields.DateField', [], {})
        },
        u'prode.team': {
            'Meta': {'object_name': 'Team'},
            'flag_image': ('sorl.thumbnail.fields.ImageField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['prode']