# Generated by Django 4.2.6 on 2023-12-01 20:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('finance', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='bank',
            field=models.ForeignKey(blank=True, db_column='staff_bank_name', null=True, on_delete=django.db.models.deletion.SET_NULL, to='finance.bank'),
        ),
        migrations.AddField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='staffdepartment', to='account.department'),
        ),
        migrations.AddField(
            model_name='staff',
            name='grade',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.employeegrade'),
        ),
        migrations.AddField(
            model_name='staff',
            name='work_place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.workplace'),
        ),
        migrations.AddField(
            model_name='headofdepartment',
            name='department',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hoddepartment', to='account.department'),
        ),
        migrations.AddField(
            model_name='headofdepartment',
            name='hod',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hodstaff', to='account.staff'),
        ),
        migrations.AddField(
            model_name='staffuser',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups'),
        ),
        migrations.AddField(
            model_name='staffuser',
            name='staff',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='account.staff'),
        ),
        migrations.AddField(
            model_name='staffuser',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions'),
        ),
        migrations.AddIndex(
            model_name='staff',
            index=models.Index(fields=['phone_number'], name='staff_phone_number_idx'),
        ),
        migrations.AddIndex(
            model_name='staff',
            index=models.Index(fields=['id_number'], name='staff_id_number_idx'),
        ),
        migrations.AddIndex(
            model_name='staff',
            index=models.Index(fields=['staff_id'], name='staff_staff_id_idx'),
        ),
    ]
