from django.contrib import admin
from .models import Day, Month, Year
# Register your models here.


class MonthsInline(admin.TabularInline):
    model = Month
    extra = 1


class DaysInline(admin.TabularInline):
    model = Day
    extra = 1


class YearAdmin(admin.ModelAdmin):
    model = Year
    list_display = ("year", "months")
    inlines = [MonthsInline]


class MonthAdmin(admin.ModelAdmin):
    model = Month
    list_display = ("month_name", "year", "totalLunch")
    inlines = [DaysInline]

    def month_name(self, obj):
        return obj.__str__()
    month_name.short_description = "month"


class DayAdmin(admin.ModelAdmin):
    model = Day
    list_display = ("day","month","spent")
    fields = (('day', 'month'), "spent")


admin.site.register(Day, DayAdmin)
admin.site.register(Month, MonthAdmin)
admin.site.register(Year, YearAdmin)
