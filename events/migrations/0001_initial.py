# Generated by Django 4.0.5 on 2022-06-11 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='EventModel',
            fields=[
                ('author', models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('title', models.CharField(max_length=70)),
                ('body', models.TextField(max_length=1000)),
                ('start_date', models.DateField()),
                ('start_time', models.DateField()),
                ('end_date', models.DateField()),
                ('end_time', models.DateField()),
                ('created_on', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
