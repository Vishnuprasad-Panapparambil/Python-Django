# Generated by Django 3.1.1 on 2020-11-18 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0014_auto_20201116_0335'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cart',
            name='price',
        ),
        migrations.AlterField(
            model_name='orders',
            name='status',
            field=models.CharField(choices=[('deliverd', 'deliverd'), ('orderrecieved', 'orderrecieved'), ('dispached', 'dispached')], default='orderrecieved', max_length=120),
        ),
    ]