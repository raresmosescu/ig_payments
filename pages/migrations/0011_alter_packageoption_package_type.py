# Generated by Django 3.2.7 on 2021-09-17 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0010_auto_20210917_1150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='packageoption',
            name='package_type',
            field=models.CharField(default='growth', max_length=15),
            preserve_default=False,
        ),
    ]
