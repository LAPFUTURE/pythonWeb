# Generated by Django 2.1.4 on 2018-12-23 07:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('item', models.CharField(max_length=20)),
                ('remark', models.CharField(max_length=40)),
            ],
        ),
    ]
