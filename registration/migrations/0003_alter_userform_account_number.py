# Generated by Django 5.1.2 on 2024-11-15 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_userform_account_number_userform_balance_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userform',
            name='account_number',
            field=models.CharField(default=0, max_length=15, unique=True),
        ),
    ]
