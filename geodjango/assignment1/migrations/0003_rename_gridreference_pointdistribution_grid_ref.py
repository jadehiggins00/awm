# Generated by Django 4.2.5 on 2023-10-15 12:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('assignment1', '0002_alter_pointdistribution_source'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pointdistribution',
            old_name='GridReference',
            new_name='Grid_Ref',
        ),
    ]