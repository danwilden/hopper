# Generated by Django 2.0.4 on 2018-04-22 17:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demoapp', '0004_auto_20180421_2037'),
    ]

    operations = [
        migrations.CreateModel(
            name='Valuation',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('high', models.FloatField(help_text='Enter amount')),
                ('middle', models.FloatField(help_text='Enter amount')),
                ('low', models.FloatField(help_text='Enter amount')),
                ('start', models.FloatField(help_text='Enter amount')),
                ('growth', models.FloatField(help_text='Enter amount')),
                ('sigma', models.FloatField(help_text='Enter amount')),
                ('mu', models.FloatField(help_text='Enter amount')),
                ('equity', models.FloatField(help_text='Enter amount')),
                ('debt', models.FloatField(help_text='Enter amount')),
                ('business', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='BisVal', to='demoapp.Business')),
            ],
        ),
    ]