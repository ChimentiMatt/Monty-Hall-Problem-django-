# Generated by Django 4.0 on 2021-12-11 07:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('appMonty', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='originalanswer',
            name='changedCorrect',
        ),
        migrations.RemoveField(
            model_name='originalanswer',
            name='changedWrong',
        ),
    ]