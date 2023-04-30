# Generated by Django 4.2 on 2023-04-30 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Regions',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('region_name', models.CharField()),
            ],
            options={
                'verbose_name': 'Region',
                'verbose_name_plural': 'Regions',
            },
        ),
        migrations.CreateModel(
            name='Tweets',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('person_name', models.CharField(blank=True, max_length=100, null=True)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('text', models.TextField()),
                ('region_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.regions')),
            ],
            options={
                'verbose_name': 'Tweet',
                'verbose_name_plural': 'Tweets',
            },
        ),
    ]