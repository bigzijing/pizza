# Generated by Django 2.0.3 on 2020-02-27 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_auto_20200227_0704'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addeditem',
            old_name='selection',
            new_name='cart',
        ),
    ]