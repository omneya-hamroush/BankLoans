# Generated by Django 2.2.16 on 2021-12-29 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_loans', '0004_auto_20211229_0309'),
    ]

    operations = [
        migrations.AddField(
            model_name='fund',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='loan',
            name='amount',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
