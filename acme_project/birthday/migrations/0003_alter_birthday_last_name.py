# Generated by Django 3.2.16 on 2024-03-17 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('birthday', '0002_auto_20240317_2044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='birthday',
            name='last_name',
            field=models.CharField(blank=True, help_text='Опциональное поле', max_length=20, verbose_name='Фамилия'),
        ),
    ]
