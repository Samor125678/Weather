from tkinter import *
import main


window = Tk()
window.title("Погода")
window.geometry("810x400")

# чтобы поля не были пустыми и пользователь понял, что в них писать


class EntryWithPlaceholder(Entry):
    def __init__(self, master=None, placeholder=None):
        super().__init__(master)

        if placeholder is not None:
            self.placeholder = placeholder
            self.placeholder_color = 'grey'
            self.default_fg_color = self['fg']

            self.bind("<FocusIn>", self.focus_in)
            self.bind("<FocusOut>", self.focus_out)

            self.put_placeholder()

    def put_placeholder(self):
        self.insert(0, self.placeholder)
        self['fg'] = self.placeholder_color

    def focus_in(self, *args):
        if self['fg'] == self.placeholder_color:
            self.delete('0', 'end')
            self['fg'] = self.default_fg_color

    def focus_out(self, *args):
        if not self.get():
            self.put_placeholder()

# сами поля


if __name__ == "__main__":

    country_name = EntryWithPlaceholder(window, 'Страна')
    state_name = EntryWithPlaceholder(window, 'Регион')
    city_name = EntryWithPlaceholder(window, 'Город')

    country_name.pack()
    state_name.pack()
    city_name.pack()


# отображаем информацию
def city_weather():

    country = country_name.get()
    state = state_name.get()
    city = city_name.get()

    conditions, temp, wind, temp_result= main.weather(city, country, state)
    conditions_label = Label(text= "Условия:  " + str(conditions), fg="#000000", bg="#ffffff", justify=LEFT)
    temp_label = Label(text= "Температура:  " + str(temp) + " С", fg="#000000", bg="#ffffff", justify=LEFT)
    wind_label = Label(text= "Ветер:  " + str(wind) + " м/с", fg="#000000", bg="#ffffff", justify=LEFT)

    conditions_label.place(relx=.1, rely=.3)
    temp_label.place(relx=.1, rely=.4)
    wind_label.place(relx=.1, rely=.5)

    clothes_label_1 = Label( fg="#000000", bg="#ffffff", justify=LEFT)
    clothes_label_2 = Label( fg="#000000", bg="#ffffff", justify=LEFT)
    clothes_label_3 = Label( fg="#000000", bg="#ffffff", justify=LEFT)

    clothes_label_1.place(relx=.1, rely=.6)
    clothes_label_2.place(relx=.1, rely=.7)
    clothes_label_3.place(relx=.1, rely=.8)

    clothes_con, clothes_temp, clothes_wind = main.clothes(conditions, temp_result, wind)

    clothes_label_1["text"] = clothes_con
    clothes_label_2["text"] = clothes_temp
    clothes_label_3["text"] = clothes_wind


button = Button(window, text="OK", command=city_weather)
button.pack()

window.mainloop()
