# Generated by Django 3.1.4 on 2020-12-22 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20201217_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.DecimalField(decimal_places=1, max_digits=3),
        ),
    ]
