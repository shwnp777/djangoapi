# Generated by Django 4.0.5 on 2022-06-11 19:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('care_group', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProfileModel',
            fields=[
                ('user', models.OneToOneField(default='1', on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('image', models.ImageField(default='default.jpg', upload_to='profile_pics')),
                ('phone_number', models.CharField(default='555-555-5555', max_length=16)),
                ('email', models.EmailField(default='empty@email.com', max_length=254)),
                ('street', models.CharField(default='No Street Address Provided', max_length=40)),
                ('city', models.CharField(default='No Street Address Provided', max_length=40)),
                ('state', models.CharField(default='No State Provided', max_length=40)),
                ('zipcode', models.CharField(default='None', max_length=9)),
                ('birthday', models.DateField(default='11/26/1980')),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Gender', max_length=6)),
                ('sunday_worship', models.BooleanField(default=False)),
                ('wednesday_worship', models.BooleanField(default=False)),
                ('sunday_singing', models.BooleanField(default=False)),
                ('wednesday_singing', models.BooleanField(default=False)),
                ('scripture_reading', models.BooleanField(default=False)),
                ('sunday_security', models.BooleanField(default=False)),
                ('sunday_technology', models.BooleanField(default=False)),
                ('wednesday_security', models.BooleanField(default=False)),
                ('wednesday_technology', models.BooleanField(default=False)),
                ('elder', models.BooleanField(default=False)),
                ('deacon', models.BooleanField(default=False)),
                ('preacher', models.BooleanField(default=False)),
                ('group_leader', models.BooleanField(default=False)),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='care_group.caremodel')),
            ],
        ),
    ]