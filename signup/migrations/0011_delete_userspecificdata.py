# Generated by Django 4.2.1 on 2023-06-07 22:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0010_userspecificdata_delete_userspecifictable'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserSpecificData',
        ),
    ]
