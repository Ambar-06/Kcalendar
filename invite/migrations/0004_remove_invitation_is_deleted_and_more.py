# Generated by Django 5.0.3 on 2024-04-06 17:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invite', '0003_invite_alter_invitation_inviter_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='invitation',
            name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='invite',
            name='is_deleted',
        ),
    ]