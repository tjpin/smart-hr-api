# Generated by Django 4.2.6 on 2023-12-01 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('directory', '0002_alter_document_document_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='formdocument',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='document',
            name='document_id',
            field=models.CharField(default='5439017593', max_length=16),
        ),
        migrations.AlterField(
            model_name='formdocument',
            name='form_id',
            field=models.CharField(default='5439017593', max_length=10, primary_key=True, serialize=False, verbose_name='Form ID'),
        ),
        migrations.AlterField(
            model_name='transmital',
            name='transmital_id',
            field=models.CharField(default='469421759310', max_length=16, primary_key=True, serialize=False),
        ),
    ]
