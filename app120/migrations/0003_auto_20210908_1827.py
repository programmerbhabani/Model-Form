# Generated by Django 3.0.1 on 2021-09-08 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app120', '0002_auto_20210908_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='email',
            field=models.EmailField(max_length=70),
        ),
    ]
