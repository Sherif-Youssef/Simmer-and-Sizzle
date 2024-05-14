# Generated by Django 5.0.4 on 2024-05-14 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("RecipeFinder", "0002_rename_ingredient_ingredient_name"),
    ]

    operations = [
        migrations.AlterField(
            model_name="recipe",
            name="course",
            field=models.CharField(
                choices=[
                    ("Appetizers", "Appetizers"),
                    ("Maincourse", "Maincourse"),
                    ("Dessert", "Dessert"),
                ],
                max_length=25,
            ),
        ),
    ]