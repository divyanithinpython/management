# Generated by Django 5.0.3 on 2024-04-13 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0045_alter_travelbook_destination'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tour_Pakage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='image/')),
                ('price', models.IntegerField()),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('shortdescription', models.TextField()),
                ('fulldescription', models.TextField()),
                ('approved', models.BooleanField(default=False, verbose_name='Approved')),
            ],
        ),
        migrations.RemoveField(
            model_name='pakageadmin',
            name='pakage_ptr',
        ),
        migrations.DeleteModel(
            name='Pakage',
        ),
        migrations.DeleteModel(
            name='PakageAdmin',
        ),
    ]