# Generated by Django 3.2.4 on 2022-01-12 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20220111_2113'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_input',
            name='role',
            field=models.CharField(blank=True, max_length=255),
        ),
        migrations.AlterField(
            model_name='user_input',
            name='name',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
