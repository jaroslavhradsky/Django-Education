# Generated by Django 4.2.5 on 2023-10-12 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='image',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='interpret',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='album',
            name='name',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
