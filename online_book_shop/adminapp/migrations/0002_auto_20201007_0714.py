# Generated by Django 3.1.1 on 2020-10-07 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(default='no name', upload_to='images'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='book',
            name='publisher',
            field=models.CharField(default='exit', max_length=100),
            preserve_default=False,
        ),
    ]
