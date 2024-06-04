# Generated by Django 5.0.6 on 2024-05-24 20:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Story',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('storyType', models.CharField(max_length=200)),
                ('gender', models.CharField(max_length=200)),
                ('characterName', models.CharField(max_length=200)),
                ('inspiration', models.CharField(max_length=200)),
                ('additionalPlotOutline', models.CharField(max_length=5000)),
                ('questionToChat', models.CharField(max_length=5000)),
            ],
        ),
    ]
