# Generated by Django 2.0.3 on 2020-02-28 16:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_auto_20200229_0028'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtraSelection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.MenuItem')),
                ('main', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.AddedItem')),
            ],
        ),
        migrations.AddField(
            model_name='addeditem',
            name='extras',
            field=models.ManyToManyField(through='orders.ExtraSelection', to='orders.MenuItem'),
        ),
    ]