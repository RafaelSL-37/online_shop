# Generated by Django 3.1.5 on 2021-01-10 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ratings', '0003_auto_20210110_2259'),
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ratings',
            field=models.ManyToManyField(blank=True, to='ratings.Rating'),
        ),
    ]
