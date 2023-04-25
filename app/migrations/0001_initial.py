# Generated by Django 4.1.7 on 2023-04-11 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='candidates',
            fields=[
                ('cid', models.AutoField(primary_key=True, serialize=False)),
                ('cname', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='interview',
            fields=[
                ('iid', models.AutoField(primary_key=True, serialize=False)),
                ('i_name', models.CharField(max_length=200)),
                ('st', models.CharField(max_length=200)),
                ('et', models.CharField(max_length=200)),
                ('cand', models.CharField(max_length=200)),
            ],
        ),
    ]