# Generated by Django 4.2.3 on 2024-02-21 15:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentAdmissionEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p_student_id', models.CharField(max_length=14)),
                ('p_semester', models.CharField(max_length=5)),
                ('p_amount', models.CharField(max_length=20)),
                ('p_money_receipt', models.CharField(max_length=25)),
                ('p_mode_payment', models.CharField(max_length=20)),
                ('p_campus', models.CharField(max_length=20)),
                ('p_date', models.CharField(max_length=20)),
                ('ip', models.CharField(blank=True, max_length=20)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
