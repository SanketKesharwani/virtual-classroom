# Generated by Django 3.0 on 2021-11-14 14:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_classroomstudentslist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='classroomstudentslist',
            old_name='studentId',
            new_name='studentList',
        ),
    ]