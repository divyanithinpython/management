# Generated by Django 5.0.3 on 2024-03-30 08:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourpackage',
            name='full_description',
        ),
    ]
