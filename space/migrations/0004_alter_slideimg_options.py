# Generated by Django 4.1 on 2023-07-26 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('space', '0003_alter_slideimg_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='slideimg',
            options={'ordering': ['img'], 'verbose_name_plural': 'Добавить фотографии в карусель'},
        ),
    ]
