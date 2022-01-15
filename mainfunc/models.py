from datetime import date

from django.db import models


class NewsOutlet(models.Model):
    name = models.CharField(max_length=32)
    tag = models.CharField(max_length=32, null=True)
    # links
    link_to = models.URLField()
    rss_source = models.URLField(default=None, blank=True, null=True)
    # stats
    year_score = models.IntegerField(default=0)
    month_score = models.IntegerField(default=0)
    week_score = models.IntegerField(default=0)
    day_score = models.IntegerField(default=0)
    year_volume = models.IntegerField(default=0)
    month_volume = models.IntegerField(default=0)
    week_volume = models.IntegerField(default=0)
    day_volume = models.IntegerField(default=0)
    year_positive_points = models.IntegerField(default=0)
    month_positive_points = models.IntegerField(default=0)
    week_positive_points = models.IntegerField(default=0)
    day_positive_points = models.IntegerField(default=0)
    year_negative_points = models.IntegerField(default=0)
    month_negative_points = models.IntegerField(default=0)
    week_negative_points = models.IntegerField(default=0)
    day_negative_points = models.IntegerField(default=0)
    # misc
    advertiser = models.CharField(max_length=32,default=None, blank=True, null=True)
    # themes
    theme1 = models.IntegerField(default=None, blank=True, null=True)
    theme2 = models.IntegerField(default=None, blank=True, null=True)
    theme3 = models.IntegerField(default=None, blank=True, null=True)

    def __str__(self):
        return self.name


class SingleDailyStat(models.Model):
    outlet = models.ForeignKey(NewsOutlet, on_delete=models.CASCADE)
    day = models.DateField(default=date.today)
    total_negative_points = models.IntegerField(default=0)
    total_positive_points = models.IntegerField(default=0)
    score = models.IntegerField(default=0)
    volume = models.IntegerField(default=0)
