# Generated by Django 4.2.16 on 2024-12-08 07:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resources', '0008_remove_assignment_assigned_personnel_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personnel',
            old_name='name',
            new_name='personnel_name',
        ),
    ]