# Generated by Django 3.2.8 on 2021-10-21 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('person', '0004_alter_person_personal_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photo'),
        ),
    ]