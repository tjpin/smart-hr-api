# Generated by Django 4.2.6 on 2023-12-01 20:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transmital',
            fields=[
                ('transmital_id', models.CharField(default='375689514432', max_length=16, primary_key=True, serialize=False)),
                ('transmital', models.FileField(upload_to='files/office/transmitals/')),
                ('purpose', models.CharField(choices=[('Un-specified', 'Default'), ('Review', 'Review'), ('Approval', 'Approval'), ('Disposal', 'Disposal'), ('Distribution', 'Distribution')], default='Un-specified', max_length=50)),
                ('date_submitted', models.DateField(default=django.utils.timezone.now)),
                ('expected_return_date', models.DateField(default=django.utils.timezone.now)),
                ('date_returned', models.DateField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('Default', 'Default'), ('In Review', 'In Review'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Submitted', 'Submitted'), ('Disposed', 'Disposed'), ('Dispatched', 'Dispatched')], default='Default', max_length=50)),
                ('approved_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='approving_user', to=settings.AUTH_USER_MODEL)),
                ('referred_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiving_user', to=settings.AUTH_USER_MODEL)),
                ('submitted_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='submiting_user', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transmital',
                'verbose_name_plural': 'Transmitals',
                'ordering': ['-date_submitted'],
            },
        ),
        migrations.CreateModel(
            name='FormDocument',
            fields=[
                ('form_id', models.CharField(default='0590795144', max_length=10, primary_key=True, serialize=False, verbose_name='Form ID')),
                ('form', models.FileField(upload_to='files/office/forms/')),
                ('date_uploaded', models.DateTimeField(auto_now_add=True)),
                ('form_type', models.CharField(choices=[('HR Form', 'Hr Form'), ('Job Application', 'Job Application'), ('Leave Application', 'Leave Application'), ('Request Form', 'Special Request Form'), ('Cash Request Form', 'Cash Request Form'), ('Cash Request Request Form', 'Cash Advanced Request Form'), ('General Form', 'General Form')], default='General Form', max_length=30)),
                ('uploaded_by', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Form Document',
                'verbose_name_plural': 'Form Documents',
                'ordering': ('-date_uploaded',),
            },
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('document_id', models.CharField(default='0590795144', max_length=16)),
                ('document_type', models.CharField(choices=[('Id', 'Id'), ('General Document', 'Default'), ('Resume', 'Resume'), ('Certificate', 'Certificate'), ('Contract', 'Contract'), ('Payslip', 'Payslip'), ('Transmital', 'Transmital'), ('Application', 'Application'), ('Purchase Order', 'Purchase Order'), ('Invoice', 'Invoice'), ('Tax Form', 'Tax Form'), ('Memo', 'Memo'), ('Audit Document', 'Audit Document'), ('Offer Letter', 'Offer Letter')], default='General Document', max_length=100)),
                ('file', models.FileField(upload_to='files/user/files/')),
                ('date_uploaded', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(choices=[('Default', 'Default'), ('In Review', 'In Review'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Submitted', 'Submitted'), ('Disposed', 'Disposed'), ('Dispatched', 'Dispatched')], default='Default', max_length=20)),
                ('is_public', models.BooleanField(default=False)),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.staff')),
            ],
            options={
                'verbose_name': 'Document',
                'verbose_name_plural': 'Documents',
            },
        ),
        migrations.CreateModel(
            name='Archive',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_archived', models.DateTimeField(auto_now_add=True)),
                ('document', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='directory.document')),
            ],
            options={
                'verbose_name': 'Archive',
                'verbose_name_plural': 'Archives',
                'ordering': ['-date_archived'],
            },
        ),
    ]
