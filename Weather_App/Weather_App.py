import customtkinter
import requests

key = open('WeatherAPI_Key.txt', 'r').read()

def retrieveWeather():
    data = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={location.get()}&units=metric&appid={key}')
    if data.json()['cod'] == '404':
        result = "Invalid Location"
    else:
        weather = data.json()['weather'][0]['description']
        temp = round(data.json()['main']['temp'])
        feels = round(data.json()['main']['feels_like'])
        highest = round(data.json()['main']['temp_max'])
        lowest = round(data.json()['main']['temp_min'])
        result = f"Weather: {weather.capitalize()} \n Temperature: {temp}°C \n Feels Like: {feels}°C \n Highest: {highest}°C \n Lowest: {lowest}°C"
        
    label2.configure(text = result)
    label2.pack(padx = 15, pady = 10)
        

#GUI / App Layout

root = customtkinter.CTk()
root.geometry("400x250")

frame = customtkinter.CTkFrame(master=root)
frame.pack(padx=30, pady=30, fill="both", expand=True)

title = customtkinter.CTkLabel(master=frame, text="Weather App")
title.pack(padx=30, pady=15)

location = customtkinter.CTkEntry(master=frame, placeholder_text="Enter a location")
location.pack(padx = 15, pady=10)

submit = customtkinter.CTkButton(master=frame, text="Submit", command=retrieveWeather)
submit.pack(padx = 15, pady=10)

label2 = customtkinter.CTkLabel(master=frame, text="")
label2.pack(padx = 15, pady = 10)

root.mainloop()
