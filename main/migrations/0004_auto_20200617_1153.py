# Generated by Django 3.0.5 on 2020-06-17 03:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_expenseslist_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expenseslist',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
