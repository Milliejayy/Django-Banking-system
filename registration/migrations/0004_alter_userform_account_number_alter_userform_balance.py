# Generated by Django 5.1.2 on 2024-11-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0003_alter_userform_account_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userform',
            name='account_number',
            field=models.CharField(editable=False, max_length=15, unique=True),
        ),
        migrations.AlterField(
            model_name='userform',
            name='balance',
            field=models.DecimalField(decimal_places=2, max_digits=15),
        ),
    ]