# Generated by Django 4.2.3 on 2023-07-30 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0007_remove_usersession_sessions_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='usersession',
            name='sessions_created',
            field=models.ManyToManyField(blank=True, to='session.sessionscreated'),
        ),
    ]
