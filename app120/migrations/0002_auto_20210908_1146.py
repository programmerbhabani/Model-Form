# Generated by Django 3.0.1 on 2021-09-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app120', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentmodel',
            name='email',
            field=models.EmailField(max_length=70, unique=True),
        ),
    ]
