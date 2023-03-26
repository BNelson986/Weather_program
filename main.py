# API KEY = 4e3463a7475785eb682835233f1485e1

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


    temp_label.configure(text=f"Temperate for {city}: {temp}")
    cond_label.configure(text=f"Conditions for {city}: {conditions}")
    wind_label.configure(text=f"Wind speed for {city}: {wind}")

    
    #   CODE API USAGE HERE


#   1.  Create GUI

window = tk.Tk()

#   Prompt for city input
city_label = tk.Label(window, text = "City: ")

#   Textbox for city entry
city_entry = tk.Entry(window)

#   Prompt for state input
state_label = tk.Label(window, text = "State: ")

#   Textbox for state entry
state_entry = tk.Entry(window)

#   Label to display requested weather information
weather_label = tk.Label(window, text="Weather information will appear here")

#   Buttons to choose between Imperial and Metric Units
units_label = tk.Label(window, text="Please choose which units you wish to see")
unitSelected = tk.StringVar()
metricButton = tk.Radiobutton(window, text="Metric Units", variable=unitSelected, value='metric')
imperialButton = tk.Radiobutton(window, text="Imperial Units", variable=unitSelected, value='imperial')

#   Submit button to submit user input
submit_button = tk.Button(window, text = "Get Weather", command=get_weather)

results_label = tk.Label(window)

temp_label = tk.Label(window)
cond_label = tk.Label(window)
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
temp_label.pack()
cond_label.pack()
wind_label.pack()

#   Start event loop
window.mainloop()