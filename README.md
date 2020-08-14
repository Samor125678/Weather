# Weather

1. Умный сервис прогноза погоды. Выбран средний уровень сложности и задание со звездочкой
2. Проектирование сервиса
    2.1. Язык программирования Python. Также необходимо отправлять API запросы и использовать Tkinter для создания графического интерфейса.
    2.2. Будет десктопное приложение.
    2.3. Данные об условиях, температуре и скорости ветра, полученные с API подставляются в текстовый шаблон 
            "Условия: ___  
            Температура: ____ С, 
            Скорость ветра: ______ м/с" 
            и показываются пользователю текстом в интерфейсе.
3. Продемонстрируйте работу сервиса.
        Запись доступна по ссылке
        https://youtu.be/_m7Nod2HQqk
4. Распишите по шагам весь процесс работы программы.
            Сервис - десктопное приложение, в котором пользователь указывает страну, регион и город. В ответ на запрос, пользователь получает в ответ погоду, а также советы по одежде.
            1)	 Пользователь вводит в поле страну, регион и необходимый город. Нажимает «Ок».
            2)	Берем значения полей. Если хотя бы одно из полей Страна или Регион не заполнено, то производится поиск только по значению, указанному в поле «Город». Значения полей вставляются в API запрос. Запрос возвращает код необходимого города.
            3)	Полученное значение кода города вставляем во второй API запрос, который будет нам возвращать информацию о погоде в указанном городе.
            4)	Если возвращается ошибка, то пользователю сообщаем, что нет данных.
            5)	Если запрос прошел успешно, то вытаскиваем из json значения погодных условия, температуру и скорость ветра.
            6)	Выводим полученные данные в виде текста в окно приложения.
            7)	Далее, на основе полученных погодных условий, температуры и ветра, советуем пользователю решения по одежде.
            8)	Выводит советы в окно приложения после значений погоды.
5. Как запустить вашу программу?
        Открываем проект “Weather” и запускаем файл “grafic.py”

