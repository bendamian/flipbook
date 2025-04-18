# Generated by Django 5.2 on 2025-04-13 19:47

import multiselectfield.db.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('video', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='video',
            name='age_groups',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('under_10', 'Under 10'), ('10_13', '10–13'), ('13_16', '13–16'), ('over_16', 'Over 16')], max_length=28),
        ),
    ]
