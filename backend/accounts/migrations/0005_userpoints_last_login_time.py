# Generated by Django 5.0.6 on 2024-07-10 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_remove_userpoints_last_login_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='userpoints',
            name='last_login_time',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
