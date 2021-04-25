# Generated by Django 3.2 on 2021-04-25 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_profile_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='pro_picture',
            field=models.ImageField(null=True, upload_to='profile/'),
        ),
    ]
