# Generated by Django 5.0.6 on 2024-07-12 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_userpoints_last_login_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='useraccount',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]