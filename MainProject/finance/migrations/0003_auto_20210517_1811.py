# Generated by Django 3.1.7 on 2021-05-17 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('finance', '0002_auto_20210516_2239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loans',
            name='intrest',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=4, null=True),
        ),
    ]