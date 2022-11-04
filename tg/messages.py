import random

from .models import Message, Uniq


def mes_lvl_2(message, r_value):
    quit_vote = rand()
    us_id = message.from_user.id
    if quit_vote == 'a':
        mes_id = rand_id_mes_1(r_value)
        result = Uniq_number(us_id, mes_id)
        mes = Uniq_profiles(message, r_value, result, us_id, mes_id)
        text = Message.objects.filter(id=mes).values('message')
        tag = Message.objects.filter(id=mes).values('tag')
        value_m = str(text[0]['message']) + str('\n') + str(tag[0]['tag'])
        return value_m
    elif quit_vote == 'b':
        mes_id = rand_id_mes_2(r_value)
        result = Uniq_number(us_id, mes_id)
        mes = Uniq_profiles(message, r_value, result, us_id, mes_id)
        text = Message.objects.filter(id=mes).values('message')
        tag = Message.objects.filter(id=mes).values('tag')
        value_m = str(text[0]['message']) + str('\n') + str(tag[0]['tag'])
        return value_m
    elif quit_vote == 'c':
        mes_id = rand_id_mes_3(r_value)
        result = Uniq_number(us_id, mes_id)

        mes = Uniq_profiles(message, r_value, result, us_id, mes_id)
        text = Message.objects.filter(id=mes).values('message')
        tag = Message.objects.filter(id=mes).values('tag')
        value_m = str(text[0]['message']) + str('\n') + str(tag[0]['tag'])
        return value_m


def Uniq_profiles(message, r_value, result, us_id, mes_id):
    try:
        if result == 1:
            b = Uniq(
                    user=us_id,
                    mes=mes_id
                    )
            b.save()
            return mes_id
        else:
            mes_lvl_2(message, r_value)
    except Exception as RecursionError:
        return 1



def Uniq_number(us_id, number):
    try:
        if Uniq.objects.filter(user=us_id, mes=number).exists() == False:
            result = 1
        else:
            result = 2
        return result
    except:
        return 'asd'


def rand_id_mes_3(r_value):
    mes_list = Message.objects.filter(level=r_value, probability=50).values('id')
    count_mes = len(mes_list)
    list_m = []
    for i in range(count_mes):
        list_m.append(mes_list[i]['id'])
    mes_id = random.choice(list_m)
    return mes_id


def rand_id_mes_1(r_value):
    mes_list = Message.objects.filter(level=r_value, probability=20).values('id')
    count_mes = len(mes_list)
    list_m = []
    for i in range(count_mes):
        list_m.append(mes_list[i]['id'])
    mes_id = random.choice(list_m)
    return mes_id


def rand_id_mes_2(r_value):
    mes_list = Message.objects.filter(level=r_value, probability=30).values('id')
    count_mes = len(mes_list)
    list_m = []
    for i in range(count_mes):
        list_m.append(mes_list[i]['id'])
    mes_id = random.choice(list_m)
    return mes_id


def rand():
    data_list = ('a', 'b', 'c')
    quit_vote_l = random.choices(data_list, weights=[0.2, 0.3, 0.5])
    quit_vote = ''.join(quit_vote_l)
    return quit_vote
