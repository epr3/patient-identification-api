# Generated by Django 2.2.7 on 2019-11-17 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('custom_authentication', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_staff',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
