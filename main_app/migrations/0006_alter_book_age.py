# Generated by Django 5.1.6 on 2025-02-23 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0005_book_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='age',
            field=models.CharField(choices=[('1-3', '1-3'), ('4-6', '4-6'), ('7-9', '7-9'), ('10-12', '10-12')], default='1-3', max_length=5),
        ),
    ]
