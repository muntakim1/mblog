# Generated by Django 2.1.5 on 2019-02-09 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_contact'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Contact',
        ),
    ]