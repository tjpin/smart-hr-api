# Generated by Django 5.0.2 on 2024-07-20 18:58

import utils.validators
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='bank',
        ),
        migrations.AlterField(
            model_name='staff',
            name='staff_id',
            field=utils.validators.TitleCaseField(default='0303847285120270', max_length=16, primary_key=True, serialize=False, unique=True),
        ),
    ]