# API KEY = 4e3463a7475785eb682835233f1485e1

import tkinter as tk

#   GOAL: DISPLAY WEATHER FOR USER SPECIFIED LOCATION
#   1.  Create GUI to prompt user for location and to display results
#   2.  Request data from API and sort into categories
#   3.  Display results within the UI 

#   Function that will execute after user input

def get_weather():
    #   Retrieve user input from text boxes
    city = city_entry.get()
    state = state_entry.get()

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

#   Submit button to submit user input
submit_button = tk.Button(window, text = "Get Weather", command=get_weather)

#   Label to display requested weather information
weather_label = tk.Label(window, text="Weather information will appear here")

#   Pack the widgets into window
city_label.pack()   
city_entry.pack()
state_label.pack()
state_entry.pack()
submit_button.pack()
weather_label.pack()

#   Start event loop
window.mainloop()