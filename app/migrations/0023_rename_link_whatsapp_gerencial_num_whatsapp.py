# Generated by Django 4.0 on 2022-03-28 15:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_alter_gerencial_nome_estabelecimento'),
    ]

    operations = [
        migrations.RenameField(
            model_name='gerencial',
            old_name='link_whatsapp',
            new_name='num_whatsapp',
        ),
    ]