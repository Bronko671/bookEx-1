# Generated by Django 3.1.2 on 2020-11-12 18:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0007_remove_order_transaction_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='orderitem',
            name='quantity',
        ),
    ]
