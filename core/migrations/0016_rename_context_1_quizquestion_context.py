# Generated by Django 4.2 on 2023-08-28 21:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_remove_quizquestion_context_2_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quizquestion',
            old_name='context_1',
            new_name='context',
        ),
    ]
