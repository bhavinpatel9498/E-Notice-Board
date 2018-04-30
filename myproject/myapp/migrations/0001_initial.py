# Generated by Django 2.0.4 on 2018-04-28 03:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='buysellpoststbl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.CharField(max_length=10000)),
                ('messagedate', models.DateField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='eventspoststbl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.CharField(max_length=10000)),
                ('messagedate', models.DateField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='officialpoststbl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.CharField(max_length=10000)),
                ('messagedate', models.DateField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
        migrations.CreateModel(
            name='sportspoststbl',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('emailid', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=300)),
                ('message', models.CharField(max_length=10000)),
                ('messagedate', models.DateField(auto_now_add=True, verbose_name='Date')),
            ],
        ),
    ]
