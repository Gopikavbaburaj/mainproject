# Generated by Django 4.0.5 on 2022-07-05 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rewrd_Management_App', '0026_remove_employee_empid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blockchain_ledger',
            name='datetime',
        ),
        migrations.AddField(
            model_name='blockchain_ledger',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blockchain_ledger',
            name='time',
            field=models.DateTimeField(auto_now=True, max_length=100),
        ),
    ]
