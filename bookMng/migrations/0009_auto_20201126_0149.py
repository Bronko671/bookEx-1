# Generated by Django 3.1.3 on 2020-11-26 01:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0008_auto_20201126_0107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(blank=True, default=1, null=True),
        ),
    ]