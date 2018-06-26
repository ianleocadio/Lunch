from django.contrib import admin


class MonthListFilter(admin.SimpleListFilter):
    title= ("Month")
    parameter_name = "month"

    def lookups(self, request, model_admin):
        return (
            (1, "Janeiro"),
            (2, "Fevereiro"),
            (3, "Março"),
            (4, "Abril"),
            (5, "Maio"),
            (6, "Junho"),
            (7, "Julho"),
            (8, "Agosto"),
            (9, "Setembro"),
            (10, "Outubro"),
            (11, "Novembro"),
            (12, "Dezembro"),
        )
    def queryset(self, request, queryset):
        if self.value():
            return queryset.filter(month=self.value())
        else:
            return queryset.all()