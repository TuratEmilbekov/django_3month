# Generated by Django 4.0 on 2021-12-23 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parser_dj', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='film',
            name='image',
            field=models.CharField(max_length=255),
        ),
    ]
