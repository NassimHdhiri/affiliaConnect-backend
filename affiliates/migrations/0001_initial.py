# Generated by Django 4.2.7 on 2023-11-27 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstName', models.CharField(max_length=255)),
                ('lastName', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('tel', models.CharField(max_length=15)),
                ('webSite', models.URLField()),
                ('trackingLink', models.URLField()),
                ('method', models.CharField(max_length=255)),
                ('rate', models.CharField(max_length=255)),
                ('commPref', models.CharField(max_length=255)),
                ('gender', models.CharField(max_length=10)),
                ('location', models.CharField(max_length=255)),
                ('field', models.CharField(max_length=255)),
                ('age', models.PositiveIntegerField()),
                ('experience', models.PositiveIntegerField()),
                ('imagePath', models.URLField(default='https://source.unsplash.com/featured/?person')),
            ],
        ),
    ]
