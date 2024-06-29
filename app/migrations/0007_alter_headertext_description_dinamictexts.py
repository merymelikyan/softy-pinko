# Generated by Django 4.2.13 on 2024-06-25 20:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_headertext_description_delete_dinamictexts'),
    ]

    operations = [
        migrations.AlterField(
            model_name='headertext',
            name='description',
            field=models.CharField(max_length=255),
        ),
        migrations.CreateModel(
            name='DinamicTexts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header_text', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.headertext')),
            ],
            options={
                'verbose_name': 'Dinamic Texts',
                'verbose_name_plural': 'Dinamic Texts',
            },
        ),
    ]
