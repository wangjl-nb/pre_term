# Generated by Django 3.1 on 2020-08-14 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_auto_20200814_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='personal_record',
            name='change',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='personal_record',
            name='comment',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='template',
            name='img',
            field=models.ImageField(blank=True, null=True, upload_to='templates/%Y/%m/%d/'),
        ),
    ]