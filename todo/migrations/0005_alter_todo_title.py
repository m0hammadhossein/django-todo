# Generated by Django 4.0.1 on 2022-01-21 14:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_todo_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='title',
            field=models.CharField(max_length=20),
        ),
    ]
