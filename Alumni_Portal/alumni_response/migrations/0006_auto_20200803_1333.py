# Generated by Django 3.0.3 on 2020-08-03 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('alumni_response', '0005_auto_20200803_1318'),
    ]

    operations = [
        migrations.AlterField(
            model_name='response',
            name='passout_year',
            field=models.IntegerField(null=True),
        ),
    ]
