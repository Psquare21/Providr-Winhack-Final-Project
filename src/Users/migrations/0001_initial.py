# Generated by Django 3.0 on 2020-03-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=20, unique=True)),
                ('email', models.EmailField(blank=True, max_length=30)),
                ('password2', models.CharField(blank=True, max_length=20)),
                ('fname', models.CharField(blank=True, max_length=20)),
                ('lname', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]
