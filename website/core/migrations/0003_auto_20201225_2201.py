# Generated by Django 3.1.4 on 2020-12-25 22:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201225_2154'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfers',
            name='userId',
            field=models.IntegerField(),
        ),
    ]