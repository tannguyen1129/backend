# Generated by Django 4.2.16 on 2024-11-27 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userauths', '0002_remove_user_full_name_remove_user_gender_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.CharField(choices=[('agency', 'Cơ quan chức năng'), ('citizen', 'Người dân')], max_length=10),
        ),
    ]
