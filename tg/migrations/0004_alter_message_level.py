# Generated by Django 4.1.2 on 2022-10-14 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0003_alter_profile_counter'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='level',
            field=models.PositiveIntegerField(choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4')], default='1'),
        ),
    ]