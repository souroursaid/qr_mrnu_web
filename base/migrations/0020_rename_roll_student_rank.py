# Generated by Django 4.0.3 on 2022-05-17 13:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0019_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='roll',
            new_name='rank',
        ),
    ]
