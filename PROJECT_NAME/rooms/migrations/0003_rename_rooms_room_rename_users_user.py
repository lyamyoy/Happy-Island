# Generated by Django 4.0.3 on 2022-03-20 01:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_users_rename_name_rooms_room_name_user_room'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Rooms',
            new_name='Room',
        ),
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
