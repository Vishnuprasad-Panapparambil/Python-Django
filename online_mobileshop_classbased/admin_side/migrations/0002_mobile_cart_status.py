# Generated by Django 3.1.1 on 2020-10-31 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_side', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mobile',
            name='cart_status',
            field=models.CharField(default='not carted', max_length=120),
        ),
    ]
