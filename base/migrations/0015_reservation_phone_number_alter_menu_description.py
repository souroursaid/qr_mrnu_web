# Generated by Django 4.0.3 on 2022-05-08 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0014_delete_waitstaff'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='menu',
            name='description',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
