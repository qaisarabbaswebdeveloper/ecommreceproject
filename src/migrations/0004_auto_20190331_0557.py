# Generated by Django 2.1.7 on 2019-03-31 05:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_offer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='offer',
            old_name='save',
            new_name='saveprice',
        ),
    ]
