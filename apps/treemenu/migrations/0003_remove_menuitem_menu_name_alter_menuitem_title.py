# Generated by Django 4.2.9 on 2024-02-03 22:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treemenu', '0002_menuitem_menu_name_alter_menuitem_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menuitem',
            name='menu_name',
        ),
        migrations.AlterField(
            model_name='menuitem',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Название'),
        ),
    ]