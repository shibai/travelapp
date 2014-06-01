# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Users'
        db.create_table(u'travelapp_users', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('email', self.gf('django.db.models.fields.EmailField')(unique=True, max_length=75)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('password', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('address', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('zipcode', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('typeT', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('phone', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('url', self.gf('django.db.models.fields.CharField')(max_length=75)),
        ))
        db.send_create_signal(u'travelapp', ['Users'])

        # Adding model 'Groups'
        db.create_table(u'travelapp_groups', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('users', self.gf('django.db.models.fields.related.ForeignKey')(related_name='owenedGroups', to=orm['travelapp.Users'])),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('typeT', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'travelapp', ['Groups'])

        # Adding M2M table for field members on 'Groups'
        m2m_table_name = db.shorten_name(u'travelapp_groups_members')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('groups', models.ForeignKey(orm[u'travelapp.groups'], null=False)),
            ('users', models.ForeignKey(orm[u'travelapp.users'], null=False))
        ))
        db.create_unique(m2m_table_name, ['groups_id', 'users_id'])

        # Adding model 'Trips'
        db.create_table(u'travelapp_trips', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=30)),
            ('groups', self.gf('django.db.models.fields.related.ForeignKey')(related_name='owenedTrips', to=orm['travelapp.Groups'])),
            ('fromLoc', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('toLoc', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('typeT', self.gf('django.db.models.fields.CharField')(max_length=30)),
            ('deleted', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('content', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'travelapp', ['Trips'])

        # Adding M2M table for field members on 'Trips'
        m2m_table_name = db.shorten_name(u'travelapp_trips_members')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('trips', models.ForeignKey(orm[u'travelapp.trips'], null=False)),
            ('users', models.ForeignKey(orm[u'travelapp.users'], null=False))
        ))
        db.create_unique(m2m_table_name, ['trips_id', 'users_id'])


    def backwards(self, orm):
        # Deleting model 'Users'
        db.delete_table(u'travelapp_users')

        # Deleting model 'Groups'
        db.delete_table(u'travelapp_groups')

        # Removing M2M table for field members on 'Groups'
        db.delete_table(db.shorten_name(u'travelapp_groups_members'))

        # Deleting model 'Trips'
        db.delete_table(u'travelapp_trips')

        # Removing M2M table for field members on 'Trips'
        db.delete_table(db.shorten_name(u'travelapp_trips_members'))


    models = {
        u'travelapp.groups': {
            'Meta': {'object_name': 'Groups'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'content': ('django.db.models.fields.TextField', [], {}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['travelapp.Users']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'typeT': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'users': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owenedGroups'", 'to': u"orm['travelapp.Users']"})
        },
        u'travelapp.trips': {
            'Meta': {'object_name': 'Trips'},
            'content': ('django.db.models.fields.TextField', [], {}),
            'deleted': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'fromLoc': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'groups': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'owenedTrips'", 'to': u"orm['travelapp.Groups']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'members': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['travelapp.Users']", 'symmetrical': 'False'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'}),
            'toLoc': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'typeT': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        },
        u'travelapp.users': {
            'Meta': {'object_name': 'Users'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'email': ('django.db.models.fields.EmailField', [], {'unique': 'True', 'max_length': '75'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'phone': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'typeT': ('django.db.models.fields.CharField', [], {'max_length': '30'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '75'}),
            'zipcode': ('django.db.models.fields.CharField', [], {'max_length': '30'})
        }
    }

    complete_apps = ['travelapp']