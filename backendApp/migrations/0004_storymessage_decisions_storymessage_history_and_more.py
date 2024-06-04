# Generated by Django 5.0.6 on 2024-06-04 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0003_story_storytitle'),
    ]

    operations = [
        migrations.AddField(
            model_name='storymessage',
            name='decisions',
            field=models.CharField(blank=True, max_length=5000000),
        ),
        migrations.AddField(
            model_name='storymessage',
            name='history',
            field=models.CharField(blank=True, max_length=5000000),
        ),
        migrations.AlterField(
            model_name='story',
            name='storyTitle',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='storymessage',
            name='content',
            field=models.CharField(max_length=5000000),
        ),
    ]
