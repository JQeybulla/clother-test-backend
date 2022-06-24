# Generated by Django 3.2.8 on 2022-06-23 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_alter_customuser_managers'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='age',
            field=models.PositiveIntegerField(default=20),
        ),
        migrations.AddField(
            model_name='customuser',
            name='height',
            field=models.FloatField(default=175),
        ),
        migrations.AddField(
            model_name='customuser',
            name='weight',
            field=models.FloatField(default=70),
        ),
    ]