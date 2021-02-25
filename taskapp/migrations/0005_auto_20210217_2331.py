# Generated by Django 3.1.5 on 2021-02-17 18:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('taskapp', '0004_auto_20210217_2324'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='task',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='taskmodel',
            name='user',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
