# Generated by Django 3.1.5 on 2021-02-18 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskapp', '0015_auto_20210218_1357'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='ta_d',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
