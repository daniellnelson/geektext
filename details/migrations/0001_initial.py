# Generated by Django 3.0.2 on 2020-03-23 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=100)),
                ('age', models.IntegerField(blank=True, default=None, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('publisher', models.CharField(max_length=100)),
                ('genre', models.CharField(max_length=30)),
                ('condition', models.CharField(blank=True, choices=[('New', 'New'), ('Used', 'Used')], max_length=10)),
                ('type', models.CharField(choices=[('Hardback', 'Hardback'), ('Paperback', 'Paperback')], max_length=10)),
                ('published_date', models.DateTimeField()),
                ('cover', models.ImageField(null=True, upload_to='uploads/')),
                ('cost', models.FloatField(blank=True, default=None, null=True)),
                ('pages', models.IntegerField(blank=True, default=None, null=True)),
                ('synopsis', models.CharField(blank=True, max_length=1000, null=True)),
                ('ISBN', models.CharField(blank=True, max_length=25, null=True)),
                ('dimensions', models.CharField(blank=True, max_length=50, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Author', to='details.Author')),
            ],
        ),
    ]
