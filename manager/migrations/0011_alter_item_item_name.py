# Generated by Django 4.0.1 on 2022-03-13 15:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0010_alter_item_exp_date_alter_item_lot_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(default='', max_length=30),
        ),
    ]
