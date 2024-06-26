# Generated by Django 5.0.4 on 2024-05-02 14:07

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('username', models.CharField(max_length=255, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('password', models.CharField(max_length=255)),
                ('token', models.UUIDField(blank=True, default=uuid.uuid4, null=True)),
                ('token_expiry', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='AuthTokens',
            fields=[
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('is_deleted', models.BooleanField(blank=True, default=False, null=True)),
                ('access_token', models.CharField(max_length=255)),
                ('refresh_token', models.CharField(blank=True, max_length=255, null=True)),
                ('expires_at', models.DateTimeField()),
                ('platform', models.IntegerField()),
                ('inviter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_auth_tokens', to='user.user')),
            ],
            options={
                'get_latest_by': 'updated_at',
                'abstract': False,
            },
        ),
    ]
