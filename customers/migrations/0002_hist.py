# Generated by Django 3.2.1 on 2021-08-13 19:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('From', models.EmailField(max_length=200, unique=True)),
                ('To', models.EmailField(max_length=200, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
    ]
