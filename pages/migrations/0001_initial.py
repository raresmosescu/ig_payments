# Generated by Django 3.2.7 on 2021-09-14 12:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PackageOption',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('price', models.IntegerField()),
                ('posts', models.IntegerField()),
                ('discount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('audience_insights_url', models.URLField()),
                ('last_insights_update', models.DateField()),
                ('trust_score', models.FloatField(default=0.0)),
                ('is_verified', models.BooleanField(default=False)),
                ('owner_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PromoPackage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=15)),
                ('page_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.page')),
            ],
        ),
        migrations.CreateModel(
            name='Promo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_url', models.URLField()),
                ('caption_url', models.URLField()),
                ('submitted_at', models.DateTimeField()),
                ('scheduled_for', models.DateTimeField()),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('option_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.packageoption')),
                ('package_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.promopackage')),
                ('page_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.page')),
            ],
        ),
        migrations.AddField(
            model_name='packageoption',
            name='package_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pages.promopackage'),
        ),
    ]