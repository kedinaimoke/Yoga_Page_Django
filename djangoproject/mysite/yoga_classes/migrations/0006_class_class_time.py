# Generated by Django 4.0.4 on 2022-05-16 14:13

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('yoga_classes', '0005_remove_class_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='class',
            name='class_time',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
