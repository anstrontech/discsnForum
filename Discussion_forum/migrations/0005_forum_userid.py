# Generated by Django 3.1.3 on 2020-11-26 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion_forum', '0004_auto_20201127_0103'),
    ]

    operations = [
        migrations.AddField(
            model_name='forum',
            name='userid',
            field=models.CharField(default='-', editable=False, max_length=200),
        ),
    ]