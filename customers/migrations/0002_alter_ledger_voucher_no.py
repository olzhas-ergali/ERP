# Generated by Django 4.2 on 2023-10-13 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ledger',
            name='voucher_no',
            field=models.CharField(default='73554718189144', max_length=14, unique=True, verbose_name='Voucher No'),
        ),
    ]
