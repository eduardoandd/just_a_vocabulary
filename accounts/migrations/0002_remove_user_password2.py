# Generated by Django 5.1.1 on 2024-10-03 14:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='password2',
        ),
    ]
