# Generated by Django 4.0 on 2021-12-23 18:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_dj', '0002_alter_film_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
