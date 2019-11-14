# Generated by Django 2.2.7 on 2019-11-14 19:03

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('custom_authentication', '0002_auto_20191113_1852'),
    ]

    operations = [
        migrations.CreateModel(
            name='RefreshToken',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=100)),
                ('expiry_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
