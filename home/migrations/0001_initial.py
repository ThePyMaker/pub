# Generated by Django 4.2.3 on 2024-02-12 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DuesAdmissionEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_id', models.CharField(max_length=14)),
                ('year', models.CharField(max_length=5)),
                ('season', models.CharField(max_length=10)),
                ('semester', models.CharField(max_length=5)),
                ('program', models.CharField(max_length=150)),
                ('amount', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]