# Generated by Django 4.0.5 on 2022-06-25 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TableName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('desc', models.TextField(max_length=500)),
                ('age', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
    ]
