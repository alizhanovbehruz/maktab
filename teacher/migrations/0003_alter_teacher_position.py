# Generated by Django 4.2.1 on 2023-05-07 05:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_alter_schooladministration_science'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='position',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.RESTRICT, to='teacher.position', verbose_name='Lavozim'),
        ),
    ]