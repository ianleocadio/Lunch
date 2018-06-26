from django.contrib import admin
from .models import Day, Month, Year
from .filters import MonthListFilter
# Register your models here.


class MonthsInline(admin.TabularInline):
    model = Month
    extra = 1


class DaysInline(admin.TabularInline):
    model = Day
    extra = 1


class YearAdmin(admin.ModelAdmin):
    model = Year
    list_display = ("year", "totalLunch")
    ordering = ("-year",)


class MonthAdmin(admin.ModelAdmin):
    model = Month
    list_display = ("month_name", "year", "totalLunch")
    list_filter = ('year', MonthListFilter)

    def month_name(self, obj):
        return obj.__str__()
    month_name.short_description = "month"


class DayAdmin(admin.ModelAdmin):
    model = Day
    list_display = ("day","month","year", "spent")
    fields = (('day', 'month'), "spent")
    list_filter = ('month__year',)


    def get_ordering(self, request):
        return ["-month", "-day"]








admin.site.register(Day, DayAdmin)
admin.site.register(Month, MonthAdmin)
admin.site.register(Year, YearAdmin)
