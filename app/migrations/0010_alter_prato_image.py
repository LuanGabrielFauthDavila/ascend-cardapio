# Generated by Django 4.0 on 2022-02-20 12:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_rename_imagem_prato_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prato',
            name='image',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
