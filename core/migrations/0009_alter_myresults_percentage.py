# Generated by Django 4.2 on 2023-08-05 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_alter_quizcategory_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myresults',
            name='percentage',
            field=models.IntegerField(),
        ),
    ]