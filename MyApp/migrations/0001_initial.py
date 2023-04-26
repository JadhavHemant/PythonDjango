# Generated by Django 4.2 on 2023-04-26 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('qualification', models.CharField(max_length=100)),
                ('persentage', models.FloatField()),
            ],
            options={
                'db_table': 'tblstudents',
            },
        ),
    ]
