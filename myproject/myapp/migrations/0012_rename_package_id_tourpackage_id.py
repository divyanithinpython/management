# Generated by Django 5.0.3 on 2024-04-02 07:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0011_remove_tourpackage_id_tourpackage_package_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tourpackage',
            old_name='package_id',
            new_name='id',
        ),
    ]