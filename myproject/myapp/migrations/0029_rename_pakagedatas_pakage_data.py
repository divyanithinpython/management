# Generated by Django 5.0.3 on 2024-04-07 14:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0028_rename_pakagedata_pakagedatas'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PakageDatas',
            new_name='Pakage_Data',
        ),
    ]
