# Generated by Django 5.0.3 on 2024-04-11 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0039_alter_pakage_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('packagename', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='img/')),
            ],
        ),
    ]
