# Generated by Django 2.1.7 on 2019-02-17 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190215_1049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='customuser',
            options={'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(default='avatars/default_avatar.jpg', upload_to='avatars', verbose_name='аватарка'),
        ),
    ]
