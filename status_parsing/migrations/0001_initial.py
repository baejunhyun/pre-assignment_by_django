# Generated by Django 2.2.5 on 2020-02-28 21:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PackageModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, unique=True, verbose_name='Package Name')),
                ('depends', models.TextField(default='', verbose_name='Dependencies')),
                ('description', models.TextField(default='', verbose_name='Description')),
            ],
        ),
    ]