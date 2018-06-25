from django.db import models
import uuid
from django.db.models import Sum, F, FloatField, Max

# Create your models here.


class Day(models.Model):
    realDate = models.DateField(auto_now=True, null=True, blank=True)
    DAYS = [(i+1,i+1) for i in range(31)]
    day = models.IntegerField(
        choices=DAYS,
        default=1,
    )
    month = models.ForeignKey("Month", on_delete=models.PROTECT)
    spent = models.FloatField(default=0.0)
    def __str__(self):
        return str(self.day)
    



class Month(models.Model):
    month = models.IntegerField()
    year = models.ForeignKey("Year", null=False, blank=False, on_delete=models.PROTECT)

    def __str__(self):
        if self.month == 1:
            return "Janeiro"
        if self.month == 2:
            return "Fevereiro"
        if self.month == 3:
            return "Março"
        if self.month == 4:
            return "Abril"
        if self.month == 5:
            return "Maio"
        if self.month == 6:
            return "Junho"
        if self.month == 7:
            return "Julho"
        if self.month == 8:
            return "Agosto"
        if self.month == 9:
            return "Setembro"
        if self.month == 10:
            return "Outubro"
        if self.month == 11:
            return "Novembro"
        if self.month == 12:
            return "Dezembro"

    def calcula_total_lunch(self):
        tot = self.day_set.all().aggregate(
            tot_ped=Sum(F('spent'), output_field=FloatField())
        )['tot_ped'] or 0
        return tot
    calcula_total_lunch.short_description = "Total Spent"

    totalLunch = property(calcula_total_lunch)

class Year(models.Model):
    year = models.IntegerField()

    def __str__(self):
        return str(self.year)

    @property
    def months(self):
        return self.month_set.all()