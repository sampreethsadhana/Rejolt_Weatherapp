from tkinter import *
from tkinter import ttk
import requests


def fetch_weather_data():
    city = city_variable.get()
    api_key = "a9732488e1632c8bd4b32ed0953c80b4"
    response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}")
    data = response.json()

    if data.get("weather"):
        W_label_value.config(text=data["weather"][0]["main"])
        des_label_value.config(text=data["weather"][0]["description"])
        temp_label_value.config(text=str(round(data["main"]["temp"] - 273.15, 2)))
        pre_label_value.config(text=data["main"]["pressure"])
    else:
        W_label_value.config(text="N/A")
        des_label_value.config(text="N/A")
        temp_label_value.config(text="N/A")
        pre_label_value.config(text="N/A")


root = Tk()
root.title("Weather Forecast")
root.configure(bg="blue")
root.geometry("500x500")

title_label = Label(root, text="Weather Forecast", font=("Times New Roman", 20, "bold"))
title_label.place(x=45, y=50, height=50, width=410)

city_variable = StringVar()
cities = ["Hyderabad", "Warangal", "Nizamabad", "Karimnagar", "Khammam", "Mahbubnagar", "Adilabad", "Suryapet", "Tandur", "Siddipet",  "Vikarabad", "Mancherial", "Ramagundam", "Nalgonda", "Bhainsa"]
city_combobox = ttk.Combobox(root, values=cities, font=("Times New Roman", 20, "bold"), textvariable=city_variable)
city_combobox.place(x=55, y=120, height=40, width=390)

W_label = Label(root, text="Weather Condition", font=("Times New Roman", 15))
W_label.place(x=20, y=240, height=30, width=200)
W_label_value = Label(root, text="", font=("Times New Roman", 15))
W_label_value.place(x=250, y=240, height=30, width=200)

des_label = Label(root, text="Description", font=("Times New Roman", 15))
des_label.place(x=20, y=280, height=30, width=200)
des_label_value = Label(root, text="", font=("Times New Roman", 15))
des_label_value.place(x=250, y=280, height=30, width=200)

temp_label = Label(root, text="Temperature (°C)", font=("Times New Roman", 15))
temp_label.place(x=20, y=320, height=30, width=200)
temp_label_value = Label(root, text="", font=("Times New Roman", 15))
temp_label_value.place(x=250, y=320, height=30, width=200)

pre_label = Label(root, text="Pressure", font=("Times New Roman", 15))
pre_label.place(x=20, y=360, height=30, width=200)
pre_label_value = Label(root, text="", font=("Times New Roman", 15))
pre_label_value.place(x=250, y=360, height=30, width=200)

fetch_button = Button(root, text="Get Weather", font=("Times New Roman", 10, "bold"), command=fetch_weather_data)
fetch_button.place(x=200, y=190, height=30, width=100)

root.mainloop()
