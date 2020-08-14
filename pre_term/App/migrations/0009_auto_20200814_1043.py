# Generated by Django 3.1 on 2020-08-14 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0008_personal_record_is_creator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='team',
            name='icon',
            field=models.ImageField(blank=True, null=True, upload_to='team_icons/%Y/%m/%d/'),
        ),
        migrations.AlterField(
            model_name='user',
            name='u_icon',
            field=models.ImageField(blank=True, null=True, upload_to='icons/%Y/%m/%d/'),
        ),
    ]
