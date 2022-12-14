# Generated by Django 4.1.2 on 2022-10-08 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Config',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('param_name', models.CharField(max_length=255, verbose_name='Наименование параметра')),
                ('param_val', models.TextField(blank=True, null=True, verbose_name='Значение параметра')),
            ],
            options={
                'verbose_name': 'Параметр бота',
                'verbose_name_plural': 'Параметры бота',
                'ordering': ['param_name'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('username', models.CharField(blank=True, max_length=32, null=True)),
                ('first_name', models.CharField(max_length=256)),
                ('last_name', models.CharField(blank=True, max_length=256, null=True)),
                ('language_code', models.CharField(blank=True, help_text="Telegram client's lang", max_length=8, null=True)),
                ('deep_link', models.CharField(blank=True, max_length=64, null=True)),
                ('is_blocked_bot', models.BooleanField(default=False)),
                ('is_banned', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_moderator', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Пользователь',
                'verbose_name_plural': 'Пользователи',
            },
        ),
    ]
