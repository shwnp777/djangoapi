from django.db import models


class ServiceModel(models.Model):
    date = models.DateField()
    service_month = models.CharField(max_length=70, default='March')
    service_year = models.CharField(max_length=70, default='1996')
    service_day = models.CharField(max_length=70, default='20')
    title = models.CharField(max_length=70, default='None')
    song_leader = models.CharField(max_length=70, default='None')
    announcements = models.CharField(max_length=70, default='None')
    opening_prayer = models.CharField(max_length=70, default='None')
    lords_supper = models.CharField(max_length=70, default='None')
    scripture_reading = models.CharField(max_length=70, default='None')
    closing_prayer = models.CharField(max_length=70, default='None')
    technology = models.CharField(max_length=70, default='None')
    security = models.CharField(max_length=70, default='None')
    day_of_week = models.CharField(
        max_length=12,
        default='Day',
        choices=[('Sunday', 'Sunday'), ('Wednesday', 'Wednesday')]
    )

    class Meta:
        ordering = ['date']

    def __str__(self):
        return f"{self.date}, {self.day_of_week}"