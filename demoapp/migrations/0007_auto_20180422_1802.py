# Generated by Django 2.0.4 on 2018-04-22 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0006_remove_valuation_growth'),
    ]

    operations = [
        migrations.AddField(
            model_name='valuation',
            name='cod',
            field=models.FloatField(default=0, help_text='Enter amount'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='valuation',
            name='eroi',
            field=models.FloatField(default=0, help_text='Enter amount'),
            preserve_default=False,
        ),
    ]
