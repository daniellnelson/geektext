# Generated by Django 3.0.2 on 2020-02-29 03:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('details', '0013_book_avg_rating'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.DecimalField(decimal_places=1, default=0, max_digits=2)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='details.Book')),
            ],
            options={
                'ordering': ['-rating'],
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='anonymous user', max_length=50, null=True)),
                ('body', models.TextField()),
                ('active', models.BooleanField(default=False)),
                ('book', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='details.Book')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
    ]
