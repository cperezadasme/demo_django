# Generated by Django 2.0.3 on 2018-03-29 23:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_remove_author_birthdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='book',
            name='editorial',
        ),
    ]
