# Generated by Django 2.2.3 on 2019-07-09 21:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blog',
            old_name='date',
            new_name='pub_date',
        ),
    ]
