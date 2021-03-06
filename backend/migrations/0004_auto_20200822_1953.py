# Generated by Django 3.1 on 2020-08-22 13:53

from django.db import migrations, models
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20200822_1349'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='choice',
            name='preferredLowestifLowestThanHighest',
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, max_length=254, unique=True, verbose_name='email address'),
        ),
        migrations.AddConstraint(
            model_name='choice',
            constraint=models.CheckConstraint(check=models.Q(preferredLowestPrice__lte=django.db.models.expressions.F('preferredHighestPrice')), name='preferredLowestPriceisLowerThanHighest'),
        ),
    ]
