# Generated by Django 4.2.6 on 2023-12-03 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('organization', models.CharField(max_length=100)),
                ('mobile_number', models.IntegerField(blank=True, null=True)),
                ('tel_number', models.IntegerField(blank=True, null=True)),
                ('address', models.TextField(blank=True, max_length=255, null=True)),
                ('zip_code', models.IntegerField(blank=True, null=True)),
                ('tag_line', models.CharField(blank=True, max_length=100, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='media/system/logo')),
                ('working_hours', models.TextField(blank=True, max_length=255, null=True)),
                ('industry', models.CharField(blank=True, max_length=100, null=True)),
                ('capital', models.DecimalField(blank=True, decimal_places=2, max_digits=16, null=True)),
                ('date_established', models.DateField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'SystemSetting',
                'verbose_name_plural': 'SystemSettings',
            },
        ),
    ]
