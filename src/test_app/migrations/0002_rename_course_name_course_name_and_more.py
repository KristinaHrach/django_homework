# Generated by Django 4.0.6 on 2022-07-20 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('test_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='course',
            old_name='course_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='subject',
            old_name='subject_name',
            new_name='name',
        ),
    ]
