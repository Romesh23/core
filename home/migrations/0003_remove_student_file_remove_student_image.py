# Generated by Django 5.0 on 2023-12-30 15:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_student_email'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='file',
        ),
        migrations.RemoveField(
            model_name='student',
            name='image',
        ),
    ]
