# Generated by Django 3.2 on 2024-03-11 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_alter_user_organizations'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AddField(
            model_name='user',
            name='username',
            field=models.CharField(default=123, max_length=50),
            preserve_default=False,
        ),
    ]
