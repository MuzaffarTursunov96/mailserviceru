# Generated by Django 3.2.16 on 2022-12-15 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_messages_created_date_to_send'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mails',
            name='end_date',
            field=models.DateTimeField(default='2022-12-15'),
        ),
        migrations.AlterField(
            model_name='mails',
            name='start_date',
            field=models.DateTimeField(default='2022-12-15'),
        ),
        migrations.AlterField(
            model_name='messages',
            name='created_date_to_send',
            field=models.DateTimeField(default='2022-12-15'),
        ),
    ]