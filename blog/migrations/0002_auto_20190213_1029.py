# Generated by Django 2.1.7 on 2019-02-13 10:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_podted',
            new_name='date_posted',
        ),
    ]
