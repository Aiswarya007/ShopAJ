# Generated by Django 5.0.1 on 2024-11-22 12:41

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("shop", "0005_cartitem"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="cart",
            name="product",
        ),
    ]
