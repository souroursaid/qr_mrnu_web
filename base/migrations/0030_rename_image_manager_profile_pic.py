# Generated by Django 4.0.3 on 2022-06-03 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0029_remove_manager_address'),
    ]

    operations = [
        migrations.RenameField(
            model_name='manager',
            old_name='image',
            new_name='profile_pic',
        ),
    ]