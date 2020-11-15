# Generated by Django 2.2.10 on 2020-10-03 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstbook', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='licence',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=240)),
                ('email', models.EmailField(max_length=250, unique=True)),
                ('postcode', models.CharField(max_length=250)),
                ('type', models.CharField(max_length=250)),
                ('ammount', models.CharField(max_length=222)),
                ('payment', models.CharField(max_length=250)),
            ],
        ),
    ]