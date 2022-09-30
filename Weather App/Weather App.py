from tkinter import * 
import requests 
import time
import json
import urllib.request

def getWeather(canvas):
    city = textfield.get()
    api = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid=32d8a864a70fd4564c382f710c3c1f05"
    json_data = requests.get(api).json()      # call json data
    condition = json_data["weather"][0]["main"]     # retrieve weather condition 
    temp = int((json_data["main"]["temp"] - 273.15) * 9/5 + 32)  # convert kelvin to fahrenheit
    min_temp = int((json_data["main"]["temp_min"] - 273.15) * 9/5 + 32)
    max_temp = int((json_data["main"]["temp_max"] - 273.15) * 9/5 + 32)
    pressure = json_data["main"]["pressure"]
    humidity = json_data["main"]["humidity"]
    wind = json_data["wind"]["speed"]
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunrise"] + 21600))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data["sys"]["sunset"] + 21600))

    final_info = condition + "\n" + str(temp) + " F"
    final_data = "\n" + "Max Temp: " + str(max_temp) + "\n" + "Min Temp: " + str(min_temp) + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "\n" + "Wind Speed: " + str(wind) + "\n" + "Sunrise: " + sunrise + "\n" + "Sunset: " + sunset
    label1.config(text = final_info)
    label2.config(text = final_data)

def getLocation():
    resource = urllib.request.urlopen('https://api.ipregistry.co/?key=5l1j91plkayy43qd')
    payload = resource.read().decode('utf-8')
    city_name = json.loads(payload)['location']['city']
    textfield.delete(0, len(textfield.get()))   # clear entry
    textfield.insert(0 ,city_name)
    getWeather(canvas)

canvas = Tk()                # define ui
canvas.geometry("600x500")      # set measurements of ui
canvas.title("Weather App")     # set title

# define fonts
f = ("poppins", 15, "bold") 
t = ("poppins", 35, "bold")

textfield = Entry(canvas, justify ="center", font = t)  # define text field
textfield.pack(pady = 20)               # organize textfield in blocks, define padding
textfield.focus()                       # focus on textfield when opening app
textfield.bind("<Return>", getWeather)  # run function when enter button is pressed

Button(canvas, text="Use My Location", command=getLocation).pack(pady=7)

label1 = Label(canvas, font = t)     # create label for data
label1.pack()                           # organize label in blocks
label2 = Label(canvas, font = f)
label2.pack()

canvas.mainloop()       # execute application