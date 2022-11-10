from typing import Dict

from django.db import models
from django.utils.translation import gettext_lazy as _


class Profile(models.Model):
    class level_profile(models.TextChoices):
        JUNIOR = 'JR', _('Junior')
        MIDDLE = 'MD', _('Middle')
        SENIOR = 'SR', _('Senior')

    level = models.CharField(
        max_length=2,
        choices=level_profile.choices,
        default=level_profile.JUNIOR,
    )
    counter = models.PositiveIntegerField(default=0)
    user_id = models.IntegerField(primary_key=True, unique=True)
    username = models.CharField(max_length=64, null=True, blank=True)
    first_name = models.CharField(max_length=256)
    last_name = models.CharField(max_length=256, null=True, blank=True)

    def __str__(self):
        return f'@{self.username}' if self.username is not None else f'{self.user_id}'

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Message(models.Model):

    class level_m(models.TextChoices):
        JUNIOR = 5, _('Junior')
        MIDDLE = 6, _('Middle')
        SENIOR = 7, _('Senior')

    class probability_v(models.TextChoices):
        twenty = 20, _('0,2')
        thirty = 30, _('0,3')
        fifty = 50, _('0,5')

    level = models.CharField(
        max_length=2,
        choices=level_m.choices,
        default=level_m.JUNIOR,
    )
    message = models.TextField()
    tag = models.CharField(max_length=255)
    probability = models.CharField(
        max_length=2,
        choices=probability_v.choices,
        default=probability_v.twenty,
    )

    def __str__(self):
        return str(self.tag) + '---level:' + str(self.level) + '---prob:' + str(self.probability)

    class Meta:
        verbose_name = 'Квест'
        verbose_name_plural = 'Квесты'


class Uniq(models.Model):
    user = models.CharField(max_length=20, db_index=True)
    mes = models.CharField(max_length=20, db_index=True)

