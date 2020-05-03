# Generated by Django 2.1.15 on 2020-05-03 07:58

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
            name='Dismiss',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dismiss_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Join',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='join_users', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='JoinMatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('home_away', models.CharField(max_length=10)),
                ('league_acl_fa', models.CharField(max_length=10)),
                ('vs', models.CharField(max_length=20)),
                ('highlight', models.BooleanField()),
                ('date', models.DateTimeField()),
                ('dismiss_match', models.ManyToManyField(related_name='dismiss_matches', to='calender.Dismiss')),
                ('join_match', models.ManyToManyField(related_name='join_matches', to='calender.Join')),
            ],
        ),
    ]
