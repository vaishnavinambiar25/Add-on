# Generated by Django 5.1 on 2024-08-24 05:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Applicant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default=None, max_length=15)),
                ('last_name', models.CharField(default=None, max_length=15)),
                ('age', models.IntegerField(default=None)),
            ],
        ),
    ]
