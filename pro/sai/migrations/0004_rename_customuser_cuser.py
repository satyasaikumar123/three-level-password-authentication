# Generated by Django 4.2 on 2023-05-04 09:27

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sai', '0003_alter_customuser_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CustomUser',
            new_name='CUser',
        ),
    ]
