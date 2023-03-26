import tkinter as tk
import requests
from uszipcode import SearchEngine

#   GOAL: DISPLAY WEATHER FOR USER SPECIFIED LOCATION
#   1.  Create GUI to prompt user for location and to display results
#   2.  Request data from API and sort into categories
#   3.  Display results within the UI 

#   Import api key

with open("API_key.txt", "r") as file:
    key = file.readline()


def get_weather():
    #   Retrieve user input from text boxes
    city = city_entry.get()
    state = state_entry.get()
    units = unitSelected.get()


    #   Retrieve zipcode for easier access of API
    search = SearchEngine()

    zipcodes = search.by_city_and_state(city, state)

    zip = zipcodes[0].zipcode

    #   URL for retrieving weather data
    url = f"https://api.openweathermap.org/data/2.5/weather?zip={zip},us&APPID={key}&units={units}"

    response = requests.get(url)

    weather_data = response.json()

    temp = weather_data['main']['temp']
    conditions = weather_data['weather'][0]['main']
    wind = weather_data['wind']['speed']
    humidity = weather_data['main']['humidity']

    if units == 'metric':
        temp_label.configure(text=f"Temperate for {city}: {temp} \xB0C", fg='#39FF14', bg='#303030')
        cond_label.configure(text=f"Conditions for {city}: {conditions}", fg='#39FF14', bg='#303030')
        wind_label.configure(text=f"Wind speed for {city}: {wind} (m/s)", fg='#39FF14', bg='#303030')
        humid_label.configure(text=f"Humidity for {city}: {humidity} %", fg='#39FF14', bg='#303030')
    elif units == 'imperial':
        temp_label.configure(text=f"Temperate for {city}: {temp} \xB0F", fg='#39FF14', bg='#303030')
        cond_label.configure(text=f"Conditions for {city}: {conditions}", fg='#39FF14', bg='#303030')
        wind_label.configure(text=f"Wind speed for {city}: {wind} (mi/hr)", fg='#39FF14', bg='#303030')
        humid_label.configure(text=f"Humidity for {city}: {humidity} %", fg='#39FF14', bg='#303030')

#   1.  Create GUI

window = tk.Tk()
window.configure(background='#303030', borderwidth=5, relief='sunken', cursor='hand2', width=100, height=200)

#   Prompt for city input
city_label = tk.Label(window, text = "City: ", fg='#39FF14', bg='#303030')

#   Textbox for city entry
city_entry = tk.Entry(window, background='#444444', foreground='#2DCC0D')

#   Prompt for state input
state_label = tk.Label(window, text = "State: ", fg='#39FF14', bg='#303030')

#   Textbox for state entry
state_entry = tk.Entry(window, background='#444444', foreground='#2DCC0D')

#   Label to display requested weather information
weather_label = tk.Label(window, text="Weather information will appear here", fg='#39FF14', bg='#303030')

#   Buttons to choose between Imperial and Metric Units
units_label = tk.Label(window, text="Please choose which units you wish to see", fg='#39FF14', bg='#303030')

unitSelected = tk.StringVar()

metricButton = tk.Radiobutton(window, text="Metric Units", variable=unitSelected, value='metric', fg='#39FF14', bg='#303030'
                              , selectcolor='#BF00FF', activebackground='#BF00FF', activeforeground='ivory')

imperialButton = tk.Radiobutton(window, text="Imperial Units", variable=unitSelected, value='imperial', fg='#39FF14', bg='#303030'
                                , selectcolor='#BF00FF', activebackground='#BF00FF', activeforeground='ivory',)

#   Submit button to submit user input
submit_button = tk.Button(window, text = "Get Weather", command=get_weather, fg='#39FF14', bg='#303030'
                                , activebackground='#BF00FF', activeforeground='ivory')

results_label = tk.Label(window)

cond_label = tk.Label(window)
temp_label = tk.Label(window)
humid_label = tk.Label(window)
wind_label = tk.Label(window)


#   Pack the widgets into window
city_label.pack()   
city_entry.pack()
state_label.pack()
state_entry.pack()
units_label.pack()
metricButton.pack()
imperialButton.pack()
submit_button.pack()
results_label.pack()
cond_label.pack()
temp_label.pack()
humid_label.pack()
wind_label.pack()

#   Start event loop
window.mainloop()