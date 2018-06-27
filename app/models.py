from django.db import models
import uuid
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.db.models import Sum, F, FloatField

# Create your models here.


class Day(models.Model):
    realDate = models.DateField(auto_now=True, null=True, blank=True)
    DAYS = [(i+1,i+1) for i in range(31)]
    day = models.IntegerField(
        choices=DAYS,
        default=1,
    )
    month = models.ForeignKey("Month", on_delete=models.CASCADE)
    spent = models.FloatField(default=0.0)
    def __str__(self):
        return str(self.day)

    @property
    def year(self):
        return self.month.year




class Month(models.Model):
    month = models.IntegerField()
    year = models.ForeignKey("Year", null=False, blank=False, on_delete=models.CASCADE)

    def __str__(self):
        if self.month == 1:
            return "January"
        if self.month == 2:
            return "February"
        if self.month == 3:
            return "March"
        if self.month == 4:
            return "April"
        if self.month == 5:
            return "May"
        if self.month == 6:
            return "June"
        if self.month == 7:
            return "July"
        if self.month == 8:
            return "August"
        if self.month == 9:
            return "September"
        if self.month == 10:
            return "October"
        if self.month == 11:
            return "November"
        if self.month == 12:
            return "December"

    def total_month(self):
        tot = self.day_set.all().aggregate(
            tot_ped=Sum(F('spent'), output_field=FloatField())
        )['tot_ped'] or 0
        return "R$: "+str(tot)
    total_month.short_description = "Total Spent"

    totalLunch = property(total_month)

class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)

    def total_year(self):
        tot = self.month_set.all().aggregate(
            tot_ped=Sum(F("day__spent"), output_field=FloatField())
        )['tot_ped'] or 0
        return "R$: "+str(tot)

    total_year.short_description = "Total Spent"
    totalLunch = property(total_year)



@receiver(post_save, sender=Month)
def set_all_days_in_month(sender, instance:Month, **kwargs):
    if instance.month == 2:
        days = (Day(day=i + 1, month=instance) for i in range(29))
    elif instance.month % 2 == 0:
        days = (Day(day=i + 1, month=instance) for i in range(30))
    else:
        days = (Day(day=i + 1, month=instance) for i in range(31))

    instance.day_set.bulk_create(days)

@receiver(post_save, sender=Year)
def set_all_months_in_year(sender, instance:Year, **kwargs):
    list = (Month(month=i+1, year=instance) for i in range(12))
    instance.month_set.bulk_create(list)
    list = instance.month_set.all()
    count = 1
    for m in list:
        if count==2:
            days = (Day(day=i+1, month=m) for i in range(29))
        elif count%2==0:
            days = (Day(day=i+1, month=m) for i in range(30))
        else:
            days = (Day(day=i+1, month=m) for i in range(31))
        m.day_set.bulk_create(days)
        count+=1




