# Generated by Django 4.2.6 on 2024-05-21 19:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0022_fiber_spelling'),
    ]

    operations = [
        migrations.RenameField(
            model_name='nutritionplan',
            old_name='goal_fibers',
            new_name='goal_fiber',
        ),
    ]
