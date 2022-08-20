from django.db import models
from django.contrib.auth.models import User
from care_group.models import CareModel


today = '11/26/1980'


class ProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, default='1')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone_number = models.CharField(max_length=16, default='555-555-5555')
    email = models.EmailField(max_length=254, default='empty@email.com')
    street = models.CharField(max_length=40, default='No Street Address Provided')
    city = models.CharField(max_length=40, default='No Street Address Provided')
    state = models.CharField(max_length=40, default='No State Provided')
    zipcode = models.CharField(max_length=9, default='None')
    birthday = models.DateField(default=today)
    gender = models.CharField(
        max_length=6,
        default='Gender',
        choices=[('Male', 'Male'), ('Female', 'Female')]
    )
    group = models.ForeignKey(CareModel, on_delete=models.CASCADE)
    sunday_worship = models.BooleanField(default=False)
    wednesday_worship = models.BooleanField(default=False)
    sunday_singing = models.BooleanField(default=False)
    wednesday_singing = models.BooleanField(default=False)
    scripture_reading = models.BooleanField(default=False)
    sunday_security = models.BooleanField(default=False)
    sunday_technology = models.BooleanField(default=False)
    wednesday_security = models.BooleanField(default=False)
    wednesday_technology = models.BooleanField(default=False)
    elder = models.BooleanField(default=False)
    deacon = models.BooleanField(default=False)
    preacher = models.BooleanField(default=False)
    group_leader = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}'s Profile"

