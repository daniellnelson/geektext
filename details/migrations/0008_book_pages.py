# Generated by Django 2.1.5 on 2020-02-04 23:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0007_book_cost'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='pages',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]
