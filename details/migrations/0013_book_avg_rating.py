# Generated by Django 3.0.2 on 2020-02-29 03:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0012_auto_20200204_2358'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='avg_rating',
            field=models.DecimalField(decimal_places=1, default=0, max_digits=2),
        ),
    ]
