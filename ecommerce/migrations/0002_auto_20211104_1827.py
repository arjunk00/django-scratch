# Generated by Django 2.2.12 on 2021-11-04 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerce', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='users',
            name='phone_no',
            field=models.IntegerField(null=True),
        ),
    ]