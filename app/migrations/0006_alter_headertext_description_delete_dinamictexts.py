# Generated by Django 4.2.13 on 2024-06-25 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_alter_dinamictexts_header_text'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headertext',
            name='description',
            field=models.CharField(max_length=250),
        ),
        migrations.DeleteModel(
            name='DinamicTexts',
        ),
    ]
