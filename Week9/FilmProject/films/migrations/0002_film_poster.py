# Generated by Django 2.2.5 on 2022-08-17 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('films', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='film',
            name='poster',
            field=models.URLField(null=True),
        ),
    ]