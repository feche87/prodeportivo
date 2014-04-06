# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Match.phase'
        db.add_column(u'prode_match', 'phase',
                      self.gf('django.db.models.fields.related.ForeignKey')(default='', to=orm['prode.Team']),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Match.phase'
        db.delete_column(u'prode_match', 'phase_id')


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
            'phase': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['prode.Team']"}),
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