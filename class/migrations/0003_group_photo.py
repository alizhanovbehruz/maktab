# Generated by Django 4.2.1 on 2023-05-11 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('class', '0002_alter_group_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='group',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]