# Generated by Django 5.0.4 on 2024-05-02 14:07

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invite',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('description', models.TextField()),
                ('start_time', models.TimeField()),
                ('end_time', models.TimeField()),
                ('platform', models.IntegerField(blank=True, null=True)),
                ('duration_in_minutes', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('invitation_date_time', models.DateTimeField(blank=True, null=True)),
                ('is_invitee_notified', models.BooleanField(blank=True, default=False, null=True)),
                ('is_inviter_notified', models.BooleanField(blank=True, default=False, null=True)),
                ('invite_status', models.IntegerField(blank=True, null=True)),
                ('reschedule_invite_id', models.UUIDField(blank=True, null=True)),
                ('is_expired', models.BooleanField(blank=True, default=False, null=True)),
                ('invitees_count', models.IntegerField(blank=True, default=0, null=True)),
                ('invitees_emails', models.JSONField(blank=True, null=True)),
                ('invitation_link', models.TextField(blank=True, null=True)),
                ('invitation_unique_id', models.CharField(blank=True, max_length=255, null=True)),
                ('inviter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invitations_sent', to='user.user')),
                ('invite_reference', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='invitations', to='invite.invite')),
            ],
            options={
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
    ]
