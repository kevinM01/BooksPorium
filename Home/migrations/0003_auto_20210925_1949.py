# Generated by Django 3.1.7 on 2021-09-25 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_upload_books'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload_books',
            name='book_price',
            field=models.CharField(default='', max_length=200),
        ),
    ]