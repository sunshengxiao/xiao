# Generated by Django 2.2.7 on 2019-11-08 04:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=48)),
                ('email', models.CharField(max_length=64)),
                ('password', models.CharField(max_length=128)),
            ],
            options={
                'db_table': 'user',
            },
        ),
    ]
