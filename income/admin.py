from django.contrib import admin
from .models import IncomeModel
# Register your models here.


class IncomeSchema(admin.ModelAdmin):
    list_display=["user","income_amount","income_type","income_date","income_description"]


admin.site.register(IncomeModel,IncomeSchema)


