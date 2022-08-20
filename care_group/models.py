from django.db import models


class CareModel(models.Model):
    group_name = models.CharField(max_length=40)

    def __str__(self):
        return self.group_name
