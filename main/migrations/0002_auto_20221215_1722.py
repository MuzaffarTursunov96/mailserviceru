# Generated by Django 3.2.16 on 2022-12-15 14:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mails',
            name='end_date',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='mails',
            name='start_date',
            field=models.DateTimeField(),
        ),
    ]
