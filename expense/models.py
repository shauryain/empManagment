from django.db import models
from django.contrib.auth.models import User

class ExpenseModel(models.Model):
    expense_amount=models.IntegerField()
    expense_type=models.CharField(max_length=30)
    expense_date=models.DateField()
    expense_description=models.TextField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='expense')
    class Meta:
        db_table="expense"

    def __str__(s):
        return s.user.username