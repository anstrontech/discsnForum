# Generated by Django 3.1.3 on 2020-11-26 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion_forum', '0006_auto_20201127_0200'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discussion',
            name='name',
        ),
        migrations.AddField(
            model_name='discussion',
            name='userid',
            field=models.CharField(default='-', editable=False, max_length=200),
        ),
    ]
