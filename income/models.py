from django.db import models
from django.contrib.auth.models import User

class IncomeModel(models.Model):
    income_amount=models.IntegerField()
    income_type=models.CharField(max_length=30)
    income_date=models.DateField()
    income_description=models.TextField(max_length=200)
    user=models.ForeignKey(User,on_delete=models.CASCADE,null=True,related_name='income')
    class Meta:
        db_table="income"


    def __str__(s):
        return s.user.username 