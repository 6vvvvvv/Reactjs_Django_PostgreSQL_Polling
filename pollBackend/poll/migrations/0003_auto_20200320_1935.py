# Generated by Django 3.0.4 on 2020-03-20 18:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0002_auto_20200320_1902'),
    ]

    operations = [
        migrations.RenameField(
            model_name='polling',
            old_name='option1',
            new_name='option',
        ),
        migrations.RenameField(
            model_name='polling',
            old_name='vote1',
            new_name='vote',
        ),
        migrations.RemoveField(
            model_name='polling',
            name='option2',
        ),
        migrations.RemoveField(
            model_name='polling',
            name='option3',
        ),
        migrations.RemoveField(
            model_name='polling',
            name='title',
        ),
        migrations.RemoveField(
            model_name='polling',
            name='vote2',
        ),
        migrations.RemoveField(
            model_name='polling',
            name='vote3',
        ),
    ]
