# Generated by Django 2.2.1 on 2022-03-20 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='director',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
