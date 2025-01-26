# Generated by Django 5.1.5 on 2025-01-26 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(max_length=50)),
                ('lname', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=200)),
                ('passwd', models.CharField(max_length=100)),
                ('age', models.IntegerField()),
            ],
        ),
    ]