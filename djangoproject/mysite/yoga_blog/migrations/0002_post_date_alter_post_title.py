# Generated by Django 4.0.4 on 2022-05-16 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('yoga_blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='date',
            field=models.DateField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=60),
        ),
    ]
