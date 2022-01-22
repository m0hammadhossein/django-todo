# Generated by Django 4.0.1 on 2022-01-20 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_todo_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='completed',
            field=models.SmallIntegerField(choices=[(1, 'Done'), (2, 'Doing'), (3, 'Undone')], default=3),
        ),
    ]
