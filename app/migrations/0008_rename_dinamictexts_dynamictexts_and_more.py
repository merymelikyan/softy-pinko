# Generated by Django 4.2.13 on 2024-06-25 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_alter_headertext_description_dinamictexts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='DinamicTexts',
            new_name='DynamicTexts',
        ),
        migrations.AlterModelOptions(
            name='dynamictexts',
            options={'verbose_name': 'Dynamic Texts', 'verbose_name_plural': 'Dynamic Texts'},
        ),
    ]
