# Generated by Django 2.1.7 on 2019-03-29 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nut',
            name='image',
            field=models.ImageField(upload_to='media/upload/'),
        ),
        migrations.AlterField(
            model_name='oil',
            name='image',
            field=models.ImageField(upload_to='media/upload/'),
        ),
        migrations.AlterField(
            model_name='pastanoodle',
            name='image',
            field=models.ImageField(upload_to='media/upload/'),
        ),
    ]
