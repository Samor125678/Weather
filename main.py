import requests

appid_country = "21e790c5f6634cc7177db8f44dea8fd5"

# Узнаем погоду в выбранном городе


def weather(city, country, state):


    s_country = country
    s_state = state
    s_city = city
    city_id = 0
    mistake = 0
    appid = "bdb97b2f69e4f3ecce5026326c6277d0"

    # определяем код города

    if s_city!= "Город" and s_country!= "Страна" and s_state!="Регион":


        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/find",
                         params={'q': {s_city, s_state, s_country}, 'type': 'like', 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            city_id = data['list'][0]['id']

        except Exception as e:

            print("Такой город не найден")
            mistake = 1
            pass
    else:

        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/find",
                               params={'q': s_city, 'type': 'like', 'units': 'metric',
                                       'lang': 'ru', 'APPID': appid})
            data = res.json()
            city_id = data['list'][0]['id']

        except Exception as e:

            print("Такой город не найден")
            mistake = 1
            pass

    if mistake != 1:

        # погода конкретного города
        try:
            res = requests.get("http://api.openweathermap.org/data/2.5/weather",
                               params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
            data = res.json()
            conditions = data['weather'][0]['description']
            temp = data['main']['temp']
            temp_max = data['main']['temp_max']
            temp_min = data['main']['temp_min']
            wind = data['wind']['speed']

            temp_result = (int(temp_max)+int(temp_min))/2

            return conditions, temp, wind, temp_result

        except Exception as e:
            print("Exception (weather):", e)
            pass
    else:
        conditions = "нет данных"
        temp = "нет данных"
        wind = "нет данных"
        temp_result = "нет данных"
        return conditions, temp, wind, temp_result


def clothes(conditions, temp_result, wind):

    clothes_con = ""
    clothes_temp = ""
    clothes_wind = ""

    if conditions!="нет данных" and temp_result!="нет данных" and wind!="нет данных":

        wind = int(wind)
        clothes_wind = ""

        # подсказка по описанию
        if conditions == "ясно":
            clothes_con = "Зонтик точно можно не брать."

        else:
            if conditions == "пасмурно" or conditions == "дождь" or conditions == "небольшой дождь" or conditions == "небольшой проливной дождь":
                clothes_con = "Возьми зонт!"

            else:
                clothes_con = "Пока даже не знаем брать или не брать зонт."

        # подсказка по температуре
        if temp_result >= 22:
            clothes_temp = 'Тут ну явно очень тепло. Одевайся легко..'

        else:
            if 15 < temp_result < 22:
                clothes_temp = 'Думаю я надела бы теплую кофту или курточку. ' \
                               'Благо у меня есть плотная толстовка, которая как раз подойдет.'

            else:
                if 0 < temp_result <= 15:
                    clothes_temp = 'Пришло время явно очень теплых вещей. Я бы надела свитер и парку.'

                else:
                    if temp_result < 0:
                        clothes_temp = 'Ну все, теперь одеваемся очень тепло чтобы не заболеть. ' \
                                       'Если будет жарко, можно снять.'

                    else:
                        clothes_temp = 'Вот тут я бы и сама растерялась.'

        # подсказка по ветру
        if wind > 2.5:
            clothes_wind = 'Учти еще есть ветер, советую взять еще что-то. Ну хотя бы шарфик.'

        return clothes_con, clothes_temp, clothes_wind

    else:
        return clothes_con, clothes_temp, clothes_wind
