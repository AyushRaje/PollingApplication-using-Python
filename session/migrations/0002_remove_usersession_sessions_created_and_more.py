# Generated by Django 4.2.3 on 2023-07-30 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('session', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usersession',
            name='sessions_created',
        ),
        migrations.AddField(
            model_name='usersession',
            name='sessions_created',
            field=models.CharField(max_length=7, null=True),
        ),
    ]
