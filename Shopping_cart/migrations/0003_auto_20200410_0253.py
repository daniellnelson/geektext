# Generated by Django 3.0.2 on 2020-04-10 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Shopping_cart', '0002_auto_20200326_1626'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='quantity',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='quantity',
            field=models.IntegerField(default=1),
        ),
    ]
