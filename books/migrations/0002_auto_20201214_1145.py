# Generated by Django 3.1.4 on 2020-12-14 11:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="book",
            old_name="publishment_year",
            new_name="publication_year",
        ),
    ]
