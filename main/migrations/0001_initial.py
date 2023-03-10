# Generated by Django 3.2.16 on 2022-12-14 17:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.CharField(max_length=50)),
                ('text_approval', models.TextField(default='')),
                ('fil_code_teg', models.CharField(max_length=255)),
                ('end_date', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date_to_send', models.CharField(max_length=50)),
                ('status', models.CharField(max_length=50)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.customer')),
                ('mail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.mails')),
            ],
        ),
    ]
