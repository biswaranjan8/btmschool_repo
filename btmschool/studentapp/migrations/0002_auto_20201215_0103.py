# Generated by Django 3.0.6 on 2020-12-14 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studentapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registermodel',
            name='gender',
            field=models.CharField(choices=[('m', 'male'), ('f', 'female')], max_length=8),
        ),
    ]
