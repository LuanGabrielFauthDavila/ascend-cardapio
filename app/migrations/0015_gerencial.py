# Generated by Django 4.0 on 2022-03-18 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_prato_disponibilidade'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gerencial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('abertura', models.IntegerField(default=18, verbose_name='Abertura')),
                ('fechamento', models.IntegerField(default=22, verbose_name='Fechamento')),
            ],
        ),
    ]