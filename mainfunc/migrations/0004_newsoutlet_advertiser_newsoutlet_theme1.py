# Generated by Django 4.0 on 2022-01-15 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainfunc', '0003_newsoutlet_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='newsoutlet',
            name='advertiser',
            field=models.CharField(blank=True, default=None, max_length=32, null=True),
        ),
        migrations.AddField(
            model_name='newsoutlet',
            name='theme1',
            field=models.IntegerField(blank=True, default=None, null=True),
        ),
    ]