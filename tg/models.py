from typing import Dict

from django.db import models
from django.utils.translation import gettext_lazy as _

from tg import utils


# class Config(models.Model):
#     """Модель настроек бота."""
#
#     param_name = models.CharField(_('Наименование параметра'), max_length=255)
#     param_val = models.TextField(_('Значение параметра'), null=True, blank=True)
#
#     def __str__(self):
#         return self.param_name
#
#     class Meta:
#         ordering = ['param_name']
#         verbose_name = 'Параметр бота'
#         verbose_name_plural = 'Параметры бота'
#
#     @classmethod
#     def load_config(cls) -> Dict[str, str]:
#         config_params = cls.objects.all()
#         result = {}
#         for config_param in config_params:
#             result[config_param.param_name] = config_param.param_val
#
#         return result
#

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
    # language_code = models.CharField(max_length=8, null=True, blank=True, help_text="Telegram client's lang")
    # deep_link = models.CharField(max_length=64, null=True, blank=True)
    #
    # is_blocked_bot = models.BooleanField(default=False)
    # is_banned = models.BooleanField(default=False)
    #
    # is_admin = models.BooleanField(default=False)
    # is_moderator = models.BooleanField(default=False)
    #
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'@{self.username}' if self.username is not None else f'{self.user_id}'

    # @classmethod
    # def get_user_and_created(cls, update, context):
    #     """ python-telegram-bot's Update, Context --> User instance """
    #     data = utils.extract_user_data_from_update(update)
    #     u, created = cls.objects.update_or_create(user_id=data["user_id"], defaults=data)
    #
    #     if created:
    #         if context is not None and context.args is not None and len(context.args) > 0:
    #             payload = context.args[0]
    #             if str(payload).strip() != str(data["user_id"]).strip():  # you can't invite yourself
    #                 u.deep_link = payload
    #                 u.save()
    #
    #     return u, created

    # @classmethod
    # def get_user(cls, update, context):
    #     u, _ = cls.get_user_and_created(update, context)
    #     return u
    #
    # @classmethod
    # def get_user_by_username_or_user_id(cls, string):
    #     """ Search user in DB, return User or None if not found """
    #     username = str(string).replace("@", "").strip().lower()
    #     if username.isdigit():  # user_id
    #         return cls.objects.filter(user_id=int(username)).first()
    #     return cls.objects.filter(username__iexact=username).first()
    #
    # def invited_users(self):  # --> User queryset
    #     return Profile.objects.filter(deep_link=str(self.user_id), created_at__gt=self.created_at)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'


class Message(models.Model):

    class level_m(models.TextChoices):
        JUNIOR = 1, _('Junior')
        MIDDLE = 2, _('Middle')
        SENIOR = 3, _('Senior')

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

