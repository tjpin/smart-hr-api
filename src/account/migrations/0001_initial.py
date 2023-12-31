# Generated by Django 4.2.6 on 2023-12-01 20:44

from django.db import migrations, models
import django.utils.timezone
import utils.validators


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='StaffUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('phone_number', models.IntegerField(unique=True)),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department_name', utils.validators.TitleCaseField(max_length=255)),
            ],
            options={
                'verbose_name': 'Department',
                'verbose_name_plural': 'Departments',
            },
        ),
        migrations.CreateModel(
            name='EmployeeGrade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade', utils.validators.TitleCaseField(max_length=30)),
            ],
            options={
                'verbose_name': 'Employee Grade',
                'verbose_name_plural': 'Employee Grades',
            },
        ),
        migrations.CreateModel(
            name='HeadOfDepartment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'Head of Department',
                'verbose_name_plural': 'Heads of Departments',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('staff_id', utils.validators.TitleCaseField(default='8235595144321021', max_length=16, primary_key=True, serialize=False, unique=True)),
                ('first_name', utils.validators.TitleCaseField(max_length=255)),
                ('middle_name', utils.validators.TitleCaseField(max_length=255)),
                ('last_name', utils.validators.TitleCaseField(max_length=255)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='staffs/profile/')),
                ('date_of_birth', models.DateField()),
                ('gender', utils.validators.TitleCaseField(choices=[('Not Specified', 'Default'), ('Male', 'Male'), ('Female', 'Female'), ('Othe', 'Other')], default='Not Specified', max_length=14)),
                ('email', models.EmailField(blank=True, max_length=254, null=True, unique=True)),
                ('phone_number', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('id_number', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('joining_date', models.DateField(default=django.utils.timezone.now)),
                ('acccess_card', utils.validators.TitleCaseField(blank=True, max_length=12, null=True, unique=True)),
                ('account_number', models.BigIntegerField(blank=True, null=True, unique=True)),
                ('education_level', utils.validators.TitleCaseField(choices=[('No Degree', 'Default'), ('Certificate', 'Certificate'), ('High School', 'High School'), ('College', 'College'), ('Diploma', 'Diploma'), ('Bachelor', 'Bachelor'), ('degree', 'Degree'), ('Masters', 'Masters'), ('Doctorate', 'Doctorate'), ('Other', 'Other')], default='No Degree', max_length=14)),
                ('status', models.CharField(choices=[('Active', 'Active'), ('Suspended', 'Suspended'), ('Terminated', 'Terminated'), ('On Hold', 'On Hold')], default='Active', max_length=20)),
                ('skills', models.TextField(blank=True, null=True)),
                ('medical_card_number', utils.validators.TitleCaseField(blank=True, max_length=12, null=True)),
            ],
            options={
                'verbose_name': 'Staff',
                'verbose_name_plural': 'Staffs',
            },
        ),
        migrations.CreateModel(
            name='WorkPlace',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('workplace_name', utils.validators.TitleCaseField(max_length=255)),
                ('address', models.TextField(blank=True, null=True)),
                ('openning_time', models.TimeField(blank=True, null=True)),
                ('clossing_time', models.TimeField(blank=True, null=True)),
                ('open_on_weekends', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'Work Location',
                'verbose_name_plural': 'Work Locations',
            },
        ),
    ]
