# Generated by Django 4.2.1 on 2023-05-07 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
