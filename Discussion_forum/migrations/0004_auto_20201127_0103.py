# Generated by Django 3.1.3 on 2020-11-26 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Discussion_forum', '0003_user_tab'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_tab',
            name='username',
            field=models.CharField(default='anonymous', max_length=200),
        ),
    ]
