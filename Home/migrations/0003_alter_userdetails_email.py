# Generated by Django 3.2.3 on 2021-06-25 11:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_auto_20210625_0734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetails',
            name='email',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
    ]