# Generated by Django 4.2.5 on 2023-10-05 04:45

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('expense', '0003_alter_expense_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='expense',
            new_name='ExpenseModel',
        ),
    ]
