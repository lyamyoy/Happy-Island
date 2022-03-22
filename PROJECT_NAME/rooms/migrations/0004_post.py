# Generated by Django 4.0.3 on 2022-03-20 06:25

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0003_rename_rooms_room_rename_users_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=280)),
                ('post_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('post_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='kuchikomi', to='rooms.user')),
            ],
        ),
    ]