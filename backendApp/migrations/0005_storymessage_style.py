# Generated by Django 5.0.6 on 2024-06-04 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backendApp', '0004_storymessage_decisions_storymessage_history_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='storymessage',
            name='style',
            field=models.CharField(blank=True, max_length=5000000),
        ),
    ]