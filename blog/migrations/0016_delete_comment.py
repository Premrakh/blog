# Generated by Django 4.1.7 on 2023-03-31 09:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
    ]
