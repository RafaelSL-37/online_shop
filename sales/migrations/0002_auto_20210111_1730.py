# Generated by Django 3.1.5 on 2021-01-11 17:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sales', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='product',
            new_name='sale_amount',
        ),
    ]
