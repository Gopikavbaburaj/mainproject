# Generated by Django 3.0.5 on 2022-05-25 08:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Rewrd_Management_App', '0006_remove_coupon_active'),
    ]

    operations = [
        migrations.CreateModel(
            name='Discount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discount_coupon', models.CharField(max_length=50)),
            ],
        ),
    ]