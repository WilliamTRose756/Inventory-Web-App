# Generated by Django 4.0.3 on 2022-03-05 22:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_alter_manager_lot_number'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Manager',
            new_name='Item',
        ),
    ]