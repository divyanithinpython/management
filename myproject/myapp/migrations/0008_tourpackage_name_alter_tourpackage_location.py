# Generated by Django 5.0.3 on 2024-04-01 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_tourpackage_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='tourpackage',
            name='name',
            field=models.CharField(default=0, max_length=50),
        ),
        migrations.AlterField(
            model_name='tourpackage',
            name='location',
            field=models.CharField(max_length=50),
        ),
    ]