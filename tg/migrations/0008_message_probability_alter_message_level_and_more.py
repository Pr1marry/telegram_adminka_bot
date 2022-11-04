# Generated by Django 4.1.2 on 2022-10-19 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tg', '0007_alter_message_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='probability',
            field=models.CharField(choices=[('20', '0,2'), ('30', '0,3'), ('50', '0,5')], default='20', max_length=2),
        ),
        migrations.AlterField(
            model_name='message',
            name='level',
            field=models.CharField(choices=[('1', 'Junior'), ('2', 'Middle'), ('3', 'Senior')], default='1', max_length=2),
        ),
        migrations.AlterField(
            model_name='profile',
            name='level',
            field=models.CharField(choices=[('JR', 'Junior'), ('MD', 'Middle'), ('SR', 'Senior')], default='JR', max_length=2),
        ),
    ]
