# Generated by Django 3.1.1 on 2020-10-08 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0002_auto_20201007_0714'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
