# Generated by Django 2.2.3 on 2019-07-11 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190709_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
