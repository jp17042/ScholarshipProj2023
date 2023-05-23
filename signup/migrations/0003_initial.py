# Generated by Django 4.1.7 on 2023-05-22 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('signup', '0002_delete_userprofile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('albumid', models.IntegerField(db_column='AlbumId', primary_key=True, serialize=False)),
                ('title', models.TextField(db_column='Title')),
                ('artistid', models.IntegerField(db_column='ArtistId')),
            ],
            options={
                'db_table': 'ross',
            },
        ),
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('artistid', models.IntegerField(db_column='ArtistId', primary_key=True, serialize=False)),
            ],
        ),
    ]