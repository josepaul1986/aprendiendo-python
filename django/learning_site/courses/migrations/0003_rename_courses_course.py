# Generated by Django 4.1.3 on 2022-12-02 21:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0002_rename_courseds_courses'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Courses',
            new_name='Course',
        ),
    ]
