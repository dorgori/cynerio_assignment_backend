# Generated by Django 4.2.8 on 2023-12-18 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cyneriotask',
            name='started',
        ),
    ]