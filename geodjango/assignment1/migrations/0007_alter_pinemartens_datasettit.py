# Generated by Django 4.2.5 on 2023-10-15 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment1', '0006_pinemartens_delete_pinemarten'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pinemartens',
            name='DatasetTit',
            field=models.CharField(blank=True, max_length=254, null=True),
        ),
    ]
