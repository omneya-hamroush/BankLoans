# Generated by Django 2.2.16 on 2021-12-31 03:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bank_loans', '0008_auto_20211231_0315'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fundapplication',
            old_name='customer',
            new_name='provider',
        ),
    ]
