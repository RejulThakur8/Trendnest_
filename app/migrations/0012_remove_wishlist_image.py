# Generated by Django 5.1.1 on 2024-11-27 19:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0011_alter_wishlist_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='wishlist',
            name='image',
        ),
    ]
