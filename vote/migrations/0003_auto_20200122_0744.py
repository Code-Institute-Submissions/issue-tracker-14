# Generated by Django 2.2.9 on 2020-01-22 07:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tickets', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote', '0002_remove_vote_vote'),
    ]

    operations = [
        migrations.AddField(
            model_name='vote',
            name='published_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='vote',
            unique_together={('ticket_id', 'user_id')},
        ),
    ]
