# Generated by Django 4.0.3 on 2022-03-07 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Webpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('added', models.DateTimeField(auto_now=True)),
                ('link', models.CharField(max_length=250)),
            ],
        ),
    ]
