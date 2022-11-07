import random

from .models import Message, Uniq, Profile


def mes_lvl_2(message, r_value):
    quit_vote = rand()
    us_id = message.from_user.id

    if quit_vote == 'a':
        mesag = mes_id_search(us_id, mes_id=rand_id_mes_1(r_value))
        print(mesag)
        if mesag is None:
            mes_lvl_2(message, r_value)
        else:
            mes = mesag
            text = Message.objects.filter(id=mes).values('message')
            tag = Message.objects.filter(id=mes).values('tag')
            value_m = str(text[0]['message']) + str('\n') + str(tag[0]['tag'])
            return value_m

    elif quit_vote == 'b':
        mesag = mes_id_search(us_id, mes_id=rand_id_mes_2(r_value))
        print(mesag)
        if mesag is None:
            mes_lvl_2(message, r_value)
        else:
            mes = mesag
            text = Message.objects.filter(id=mes).values('message')
            tag = Message.objects.filter(id=mes).values('tag')
            value_m = str(text[0]['message']) + str('\n') + str(tag[0]['tag'])
            return value_m

    elif quit_vote == 'c':
        mesag = mes_id_search(us_id, mes_id=rand_id_mes_3(r_value))
        print(mesag)
        if mesag is None:
            mes_lvl_2(message, r_value)
        else:
            mes = mesag
            text = Message.objects.filter(id=mes).values('message')
            tag = Message.objects.filter(id=mes).values('tag')
            value_m = str(text[0]['message']) + str('\n') + str(tag[0]['tag'])
            return value_m


def mes_id_search(us_id, mes_id):
    result = Uniq_number(us_id, mes_id)
    mes = Uniq_profiles(result, us_id, mes_id)
    return mes


def Uniq_profiles(result, us_id, mes_id):
    if result == 'valid':
        b = Uniq(
                user=us_id,
                mes=mes_id
                )
        b.save()
        return mes_id
    elif result == 'invalid':
        return None


def Uniq_number(us_id, number):
    # try:
        result = Uniq.objects.filter(user=us_id, mes=number).exists()
        if result is False:
            return 'valid'
        elif result is True:
            return 'invalid'
    # except:
    #     return 'invalid'


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


# def valid_text(message, value_m):
#     value = value_m
#     if len(value) > 1:
#         return value
#     else:
#         return value