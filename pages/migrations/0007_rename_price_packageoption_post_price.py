# Generated by Django 3.2.7 on 2021-09-14 12:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_alter_packageoption_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='packageoption',
            old_name='price',
            new_name='post_price',
        ),
    ]
