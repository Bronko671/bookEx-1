# Generated by Django 3.1.2 on 2020-11-12 17:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0006_order_orderitem_shippingaddress'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='transaction_id',
        ),
    ]
