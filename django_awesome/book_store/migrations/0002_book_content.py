# Generated by Django 4.0.1 on 2022-01-16 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='content',
            field=models.CharField(default=None, max_length=1000),
        ),
    ]