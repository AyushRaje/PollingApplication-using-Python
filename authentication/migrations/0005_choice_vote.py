# Generated by Django 3.2.20 on 2023-07-13 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0004_alter_question_users_answered'),
    ]

    operations = [
        migrations.AddField(
            model_name='choice',
            name='vote',
            field=models.IntegerField(default=0),
        ),
    ]
