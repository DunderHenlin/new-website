# Generated by Django 3.1.2 on 2020-10-04 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=100)),
                ('Data', models.DateField()),
                ('Description', models.CharField(max_length=250)),
            ],
        ),
    ]
