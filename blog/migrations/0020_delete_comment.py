# Generated by Django 4.1.7 on 2023-04-01 04:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0019_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
