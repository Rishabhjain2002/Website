# Generated by Django 3.0.3 on 2020-02-24 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20200223_2342'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='avatar',
            field=models.ImageField(blank=True, default='default_profile_pic.png', null=True, upload_to='avatar_images'),
        ),
    ]
