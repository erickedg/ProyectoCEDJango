# Generated by Django 4.2 on 2023-04-28 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=70)),
                ('last_name', models.CharField(max_length=70)),
                ('email', models.EmailField(max_length=254)),
                ('age', models.IntegerField()),
                ('grade', models.CharField(max_length=50)),
            ],
        ),
    ]