# Generated by Django 3.0.6 on 2020-09-06 03:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50, verbose_name='First name')),
                ('minName', models.CharField(max_length=50, verbose_name='Miduim name')),
                ('lname', models.CharField(max_length=50, verbose_name='Last name')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('phone', models.CharField(max_length=50, verbose_name='phone number')),
                ('nationalno', models.CharField(max_length=50, verbose_name='national number')),
            ],
            options={
                'verbose_name': 'Customer',
                'verbose_name_plural': 'Customers',
            },
        ),
    ]