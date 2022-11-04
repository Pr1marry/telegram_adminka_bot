from .messages import mes_lvl_2
from .models import Profile


def check_and_add_user(message):
    if Profile.objects.filter(user_id=message.from_user.id):
        print('------существующий польз------')
    else:
        print('------новый польз, запись в бд...------')
        new_acc = Profile(
            first_name=message.from_user.first_name,
            last_name=message.from_user.last_name,
            user_id=message.from_user.id,
            username=message.from_user.username,
        )
        new_acc.save()


def check_value(message):
    user_counter = Profile.objects.get(user_id=message.from_user.id)
    level_user = user_counter.level
    if level_user == 'JR':
        return mes_lvl_2(message, 1)
    elif level_user == 'MD':
        return mes_lvl_2(message, 2)
    elif level_user == 'SR':
        return mes_lvl_2(message, 3)


def check_counter(message):
    user_c = Profile.objects.get(user_id=message.from_user.id)
    user_c.counter += 1
    if user_c.counter == 30:
        user_c.level = 'MD'
    elif user_c.counter == 60:
        user_c.level = 'SR'
    user_c.save()


def check_lvl_user(message, number_quest_lvl):
    user_lvl = Profile.objects.get(user_id=message.from_user.id)

    if user_lvl.counter <= 30 and number_quest_lvl == 1:
        exit = Jun(message)
    elif user_lvl.counter <= 60 and number_quest_lvl == 1:
        exit = Jun(message)
    elif user_lvl.counter > 60 and number_quest_lvl == 1:
        exit = Jun(message)
    elif user_lvl.counter <= 60 and number_quest_lvl == 2:
        exit = Mid(message)
    elif user_lvl.counter > 60 and number_quest_lvl == 2:
        exit = Mid(message)
    elif user_lvl.counter > 60 and number_quest_lvl == 3:
        exit = Sen(message)
    else:
        exit = 'Недостаточно выполненных квестов для перехода на этот уровень'

    return exit


def Jun(message):
    lvl = Profile.objects.get(user_id=message.from_user.id)
    lvl.level = 'JR'
    lvl.save()
    return '5 уровень квестов'


def Mid(message):
    lvl = Profile.objects.get(user_id=message.from_user.id)
    lvl.level = 'MD'
    lvl.save()
    return '6 уровень квестов'


def Sen(message):
    lvl = Profile.objects.get(user_id=message.from_user.id)
    lvl.level = 'SR'
    lvl.save()
    return '7 уровень квестов'


