# Generated by Django 2.2.16 on 2021-12-28 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_loans', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fund',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.FloatField(blank=True, null=True)),
                ('minimum', models.FloatField(blank=True, null=True)),
                ('maximum', models.FloatField(blank=True, null=True)),
                ('interest_rate', models.FloatField(blank=True, null=True)),
                ('duration', models.FloatField(blank=True, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='loan',
            name='duration',
            field=models.FloatField(blank=True, null=True),
        ),
    ]