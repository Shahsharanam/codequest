# Generated by Django 4.2.5 on 2024-09-03 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Design', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMst',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Email', models.EmailField(max_length=30)),
                ('ContactNo', models.CharField(max_length=15)),
                ('Username', models.CharField(max_length=40)),
                ('Password', models.CharField(max_length=10)),
            ],
        ),
    ]
