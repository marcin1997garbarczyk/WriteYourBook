# Generated by Django 5.0.6 on 2024-06-19 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0009_story_ownerid'),
    ]

    operations = [
        migrations.AddField(
            model_name='story',
            name='language',
            field=models.CharField(blank=True, max_length=5000),
        ),
    ]
