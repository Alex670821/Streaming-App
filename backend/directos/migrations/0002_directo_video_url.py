# Generated by Django 5.0.6 on 2024-07-17 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='directo',
            name='video_url',
            field=models.URLField(default='https://www.youtube.com/embed/dQw4w9WgXcQ'),
        ),
    ]
