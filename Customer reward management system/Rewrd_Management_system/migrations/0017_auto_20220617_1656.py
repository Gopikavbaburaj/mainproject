# Generated by Django 3.2 on 2022-06-17 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rewrd_Management_App', '0016_auto_20220617_1636'),
    ]

    operations = [
        migrations.AddField(
            model_name='coupon',
            name='endvalue',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='coupon',
            name='startvalue',
            field=models.IntegerField(null=True),
        ),
    ]
