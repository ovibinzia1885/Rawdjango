# Generated by Django 2.2.10 on 2020-10-17 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firstbook', '0003_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='Apply',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('throwby', models.CharField(max_length=300)),
                ('a_name', models.CharField(max_length=100)),
                ('a_email', models.EmailField(max_length=254)),
                ('a_phone', models.PositiveIntegerField()),
                ('a_type', models.CharField(max_length=100)),
                ('a_adress', models.CharField(max_length=100)),
                ('a_ward', models.PositiveIntegerField()),
                ('a_messur', models.CharField(max_length=100)),
                ('photo', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('a_pyment', models.CharField(max_length=100)),
                ('list_date', models.DateTimeField(auto_now_add=True)),
                ('update', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]