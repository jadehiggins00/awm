# Generated by Django 4.2.5 on 2023-10-16 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment1', '0011_pinemartens_latitude_pinemartens_longitude'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pinemartens',
            name='SAMPLE_YEA',
            field=models.DecimalField(blank=True, decimal_places=11, max_digits=19, null=True),
        ),
    ]