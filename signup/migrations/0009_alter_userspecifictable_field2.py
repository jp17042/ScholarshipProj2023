# Generated by Django 4.1.7 on 2023-05-22 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('signup', '0008_userspecifictable_delete_album'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userspecifictable',
            name='field2',
            field=models.IntegerField(null=True),
        ),
    ]
