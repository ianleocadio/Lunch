from django.db import models
import calendar
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
    @property
    def weekday(self):
        try:
            weekday = calendar.weekday(self.year.year, self.month.month, self.day)
            if weekday == 0:
                return "Mon"
            elif weekday == 1:
                return "Tue"
            elif weekday == 2:
                return "Wed"
            elif weekday == 3:
                return "Thu"
            elif weekday == 4:
                return "Fri"
            elif weekday == 5:
                return "Sat"
            elif weekday == 6:
                return "Sun"
            else:
                return ""
        except ValueError:
            return ""

    @property
    def weekdayNumber(self):
        try:
            return calendar.weekday(self.year.year, self.month.month, self.day)
        except ValueError:
            return ""




class Month(models.Model):
    month = models.IntegerField()
    balance = models.FloatField(default=0.0)
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

    def mini(self):
        if self.month == 1:
            return "Jan"
        if self.month == 2:
            return "Feb"
        if self.month == 3:
            return "Mar"
        if self.month == 4:
            return "Apr"
        if self.month == 5:
            return "May"
        if self.month == 6:
            return "Jun"
        if self.month == 7:
            return "Jul"
        if self.month == 8:
            return "Aug"
        if self.month == 9:
            return "Sep"
        if self.month == 10:
            return "Oct"
        if self.month == 11:
            return "Nov"
        if self.month == 12:
            return "Dec"

    def total_month(self):
        tot = self.day_set.all().aggregate(
            tot_ped=Sum(F('spent'), output_field=FloatField())
        )['tot_ped'] or 0.0
        return round(tot,2)
    total_month.short_description = "Total Spent"

    totalLunch = property(total_month)

    def balaceDep(self):
        bMonthSpent = self.year.month_set.filter(month__lte=self.month, year__year=self.year.year).aggregate(
            bMonth=Sum(F('day__spent'), output_field=FloatField())
        )['bMonth'] or 0.0

        bMonthsBalance = self.year.month_set.filter(month__lte=self.month, year__year=self.year.year).aggregate(
            bMonths=Sum(F('balance'), output_field=FloatField())
        )['bMonths'] or 0.0

        return round(bMonthsBalance - bMonthSpent,2)

class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)

    def total_year(self):
        tot = self.month_set.all().aggregate(
            tot_ped=Sum(F("day__spent"), output_field=FloatField())
        )['tot_ped'] or 0.0
        return round(tot,2)

    total_year.short_description = "Total Spent"
    totalLunch = property(total_year)



@receiver(post_save, sender=Month)
def set_all_days_in_month(sender, instance:Month, **kwargs):
    monthObj = Month.objects.get(month=instance.month, year__year=instance.year.year)

    if monthObj.day_set.count() != 0:
        return

    r = calendar.monthrange(instance.year.year, instance.month)[1]
    days = (Day(day=i + 1, month=instance) for i in range(r))

    instance.day_set.bulk_create(days)

@receiver(post_save, sender=Year)
def set_all_months_in_year(sender, instance:Year, **kwargs):

    yearObj = Year.objects.get(year=instance.year)

    if yearObj.month_set.count() != 0:
        return

    list = (Month(month=i+1, year=instance) for i in range(12))
    instance.month_set.bulk_create(list)
    list = instance.month_set.all()
    for m in list:
        r = calendar.monthrange(m.year.year, m.month)[1]
        days = (Day(day=i+1, month=m) for i in range(r))
        m.day_set.bulk_create(days)




