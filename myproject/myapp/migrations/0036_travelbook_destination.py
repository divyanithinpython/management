# Generated by Django 5.0.3 on 2024-04-08 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0035_travelbook'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelbook',
            name='destination',
            field=models.CharField(default=True, max_length=50),
        ),
    ]