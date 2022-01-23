from tkinter import *
from tkinter import messagebox
import requests


#API URL
url_api = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={note - This code wont run unless you enter your weather api key}"

#function to fetch the required information and converting it to a python object -- Dict
def weather_find(city):
    weather1 = requests.get(url_api.format(city))
    weather_dict = weather1.json()
    if weather1 :
        city = weather_dict['name']
        country_name = weather_dict["sys"]["country"]
        k_temp = weather_dict["main"]["temp"]
        c_temp = k_temp - 273.15
        f_temp = (k_temp - 273.15)*9/5+32
        weather_display = weather_dict["weather"][0]["main"]
        result = (city,country_name,c_temp,f_temp,weather_display)
        return result
    else:
        print("no details found")


#function to print the fetched values
def print_weather():
    city = city_text.get()
    weather = weather_find(city)
    if weather:
        location_entry['text'] = '{} ,{}'.format(weather[0], weather[1])
        Temperature_entry['text'] = '{:.2f} C , {:.2f} F'.format(weather[2], weather[3])
        Weather_entry['text'] = weather[4]
    else:
        messagebox.showerror("Error","Please enter a valid city name ! ! !")

#GUI window
app = Tk()
app.title("Weather App")
app.config(background="sky blue")
app.geometry('450x300')
app.resizable(False,False)


#Buttons and Labels
city_text = StringVar()
blank =Label(app, width=1,background="sky blue")
blank.pack()
entry_text = Entry(app,textvariable=city_text,background="Light Yellow",fg="Brown", font=("Arial",25,"bold"))
entry_text.pack()
blank =Label(app, width=1,background="sky blue")
blank.pack()
search_city =Button(app,text="SEARCH", width=8, fg="Brown", font=("Arial",15,"bold"),command=print_weather)
search_city.pack()
blank =Label(app, width=1,background="sky blue")
blank.pack()
location_entry = Label(app,text = '',background="sky blue",font=("Arial",25,"bold"),fg = "Brown")
location_entry.pack()
Temperature_entry = Label(app,text = '',background="sky blue",font=("Arial",25,"bold"),fg = "Brown")
Temperature_entry.pack()
Weather_entry = Label(app,text = '',background="sky blue",font=("Arial",25,"bold"),fg = "Brown")
Weather_entry.pack()

#closing the tinkter window loop 
app.mainloop()
