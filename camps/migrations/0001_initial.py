# Generated by Django 2.2.6 on 2019-10-17 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('district', models.CharField(max_length=100, null=True)),
                ('state', models.CharField(max_length=100, null=True)),
            ],
        ),
    ]
