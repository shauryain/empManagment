from django.contrib import admin
from .models import ExpenseModel
# Register your models here.


class ExpenseSchema(admin.ModelAdmin):
    list_display=["user","id","expense_amount","expense_type","expense_date","expense_description"]
admin.site.register(ExpenseModel,ExpenseSchema)