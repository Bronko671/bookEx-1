# Generated by Django 3.1.3 on 2020-11-27 00:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookMng', '0012_auto_20201127_0033'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='book',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='bookMng.book'),
        ),
    ]
