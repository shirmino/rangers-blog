# Generated by Django 3.0.3 on 2020-03-12 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_auto_20200312_1601'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='article',
            new_name='post',
        ),
    ]