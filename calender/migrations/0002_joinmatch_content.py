# Generated by Django 2.1.15 on 2020-05-05 06:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='joinmatch',
            name='content',
            field=models.TextField(default=''),
        ),
    ]
