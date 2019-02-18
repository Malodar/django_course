# Generated by Django 2.1.7 on 2019-02-15 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='avatar',
            field=models.ImageField(blank=True, upload_to='uploads/avatars/', verbose_name='аватарка'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='money',
            field=models.DecimalField(decimal_places=2, default=100, max_digits=20, verbose_name='счет'),
        ),
    ]
