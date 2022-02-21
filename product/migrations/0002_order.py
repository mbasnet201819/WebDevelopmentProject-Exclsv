# Generated by Django 4.0.2 on 2022-02-21 05:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False)),
                ('fullname', models.CharField(max_length=100)),
                ('phonenumber', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'order',
            },
        ),
    ]