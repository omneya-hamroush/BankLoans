# Generated by Django 2.2.16 on 2021-12-29 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_loans', '0002_auto_20211228_2016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fund',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='loan',
            name='duration',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
