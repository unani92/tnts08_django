# Generated by Django 2.1.15 on 2020-05-06 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calender', '0002_joinmatch_content'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='joinmatch',
            name='highlight',
        ),
    ]
