# Generated by Django 4.0 on 2022-03-20 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_alter_gerencial_options_gerencial_main_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='gerencial',
            name='logo',
            field=models.TextField(blank=True, max_length=255),
        ),
    ]
