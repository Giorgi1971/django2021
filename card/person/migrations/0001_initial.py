# Generated by Django 3.2.8 on 2021-10-20 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_nunber', models.CharField(max_length=9, unique=True)),
                ('first_name', models.CharField(max_length=48)),
                ('last_name', models.CharField(max_length=48)),
                ('photo', models.ImageField(upload_to='photo')),
                ('Citizen', models.CharField(max_length=24)),
                ('sex', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('personal_number', models.SmallIntegerField(unique=True)),
                ('Birth_date', models.DateField()),
                ('expiry_date', models.DateField()),
                ('Birth_place', models.CharField(max_length=120)),
                ('issue_date', models.DateField()),
                ('issuing_authority', models.CharField(max_length=256)),
            ],
        ),
    ]