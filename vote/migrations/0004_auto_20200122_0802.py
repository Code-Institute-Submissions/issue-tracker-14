# Generated by Django 2.2.9 on 2020-01-22 08:02

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote', '0003_auto_20200122_0744'),
    ]

    operations = [
        migrations.RenameField(
            model_name='vote',
            old_name='ticket_id',
            new_name='vote_for',
        ),
        migrations.RenameField(
            model_name='vote',
            old_name='user_id',
            new_name='voter',
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('vote_for', 'voter')},
        ),
    ]
