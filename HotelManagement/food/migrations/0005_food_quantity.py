# Generated by Django 2.2.5 on 2021-03-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0004_food_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='food',
            name='quantity',
            field=models.PositiveIntegerField(default=1),
        ),
    ]
