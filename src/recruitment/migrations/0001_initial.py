# Generated by Django 4.2.6 on 2023-12-03 15:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('address', models.CharField(blank=True, max_length=255, null=True)),
                ('resume', models.FileField(blank=True, null=True, upload_to='files/applications/resumes/')),
                ('cover_letter', models.FileField(blank=True, null=True, upload_to='files/applications/cover_letters/')),
                ('source', models.CharField(choices=[('Other', 'Other'), ('Job Board', 'Job Board'), ('Referral', 'Referral'), ('Web Search', 'Web Search')], default='Other', max_length=255)),
                ('status', models.CharField(choices=[('Default', 'Default'), ('In Review', 'In Review'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Submitted', 'Submitted'), ('Disposed', 'Disposed'), ('Dispatched', 'Dispatched')], default='Default', max_length=50)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'Candidate',
                'verbose_name_plural': 'Candidates',
            },
        ),
        migrations.CreateModel(
            name='JobPosition',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_number', models.CharField(default=5547830896, max_length=16)),
                ('title', models.CharField(max_length=255)),
                ('description', models.TextField(verbose_name='job description separated by hyphen(-)')),
                ('skills', models.TextField(verbose_name='skills separated by hyphen(-)')),
                ('experience_level', models.CharField(blank=True, max_length=100, null=True)),
                ('salary_range', models.CharField(blank=True, max_length=30, null=True)),
                ('location', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Closed', max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.department')),
            ],
            options={
                'verbose_name': 'Job Position',
                'verbose_name_plural': 'Job Positions',
            },
        ),
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_openings', models.PositiveIntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('status', models.CharField(choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open', max_length=12)),
                ('job_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.jobposition')),
            ],
            options={
                'verbose_name': 'Vacancy',
                'verbose_name_plural': 'Vacancies',
                'ordering': ['-start_date'],
            },
        ),
        migrations.CreateModel(
            name='Interview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_date', models.DateTimeField()),
                ('interview_type', models.CharField(choices=[('On Site', 'On Site'), ('Online', 'Online')], default='On Site', max_length=12)),
                ('feedback', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('Scheduled', 'Scheduled'), ('Completed', 'Completed'), ('Rejected', 'Rejected')], default='Scheduled', max_length=50)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.candidate')),
                ('interviewers', models.ManyToManyField(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Interview',
                'verbose_name_plural': 'Interviews',
                'ordering': ['-interview_date'],
            },
        ),
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application_date', models.DateField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Default', 'Default'), ('In Review', 'In Review'), ('Approved', 'Approved'), ('Rejected', 'Rejected'), ('Pending', 'Pending'), ('Submitted', 'Submitted'), ('Disposed', 'Disposed'), ('Dispatched', 'Dispatched')], default='Submitted', max_length=15)),
                ('notes', models.TextField(blank=True, null=True)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.candidate')),
                ('job_position', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='recruitment.jobposition')),
            ],
            options={
                'verbose_name': 'Application',
                'verbose_name_plural': 'Applications',
                'ordering': ['-application_date'],
            },
        ),
    ]
