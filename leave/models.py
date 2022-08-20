from django.db import models
import uuid
from django.contrib.auth.models import User

# Create your models here.


class LeaveModel(models.Model):
    # leave_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return f"{self.user.last_name}, {self.user.first_name}, {self.start_date} to {self.end_date}"

