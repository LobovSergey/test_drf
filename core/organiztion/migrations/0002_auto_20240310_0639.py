# Generated by Django 3.2 on 2024-03-10 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organiztion', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='organization',
            options={'ordering': ['title'], 'verbose_name': 'Организация', 'verbose_name_plural': 'Организации'},
        ),
        migrations.AlterField(
            model_name='organization',
            name='description',
            field=models.TextField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='organization',
            name='postcode',
            field=models.PositiveIntegerField(),
        ),
    ]
