# Generated by Django 3.2.13 on 2022-06-28 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='approved',
            field=models.BooleanField(default=False),
        ),
    ]
