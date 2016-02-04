
import tkinter as tk 
import time 
import urllib.request
import feedparser
from tkinter import *


def update_timeText(): 
    #weather
    # read weather information
    weatherURL1 = 'http://weather.yahooapis.com/forecastrss?w=1132599&u=c'
    #response1 = urllib.request.urlopen(weatherURL1)
    #html1 = response1.read()
    
    # weather parsing
    d = feedparser.parse(weatherURL1)
    location  = d.feed.yweather_location
    atmosphere = d.feed.yweather_atmosphere
    astronomy = d.feed.yweather_astronomy
    city = location['city']
    humidity = atmosphere['humidity']
    sunrise = astronomy['sunrise']
    sunset = astronomy['sunset']    
    summary = d.entries[0].summary
    temp = summary.split("High: ")
    temp = temp[1].split(" Low: ")
    high = temp[0]
    low = temp[1].split("<br />")[0]
    print ("Weather for "+city)
    print ("Low Temp:  "+low)
    print ("High Temp: "+high)
    print ("Humidity:  "+humidity)
    print ("Sunrise:   "+sunrise)
    print ("Sunset:    "+sunset)
    
    City_text = "Weather for "+city
    TempLow_text = "Low Temp:  "+low
    TempHigh_text = "High Temp: "+high
    Humidity_text = "Humidity:  "+humidity

    # for clock...    
    
    current = time.strftime("%H:%M:%S") 
    # Update the timeText Label box with the current time 
    timeText.configure(text=current) 
    # Call the update_timeText() function after 1 second 
    root.after(1000, update_timeText) 

root = tk.Tk() 
root.wm_title("Simple Clock Example") 


# Create a timeText Label (a text box) 
timeText = tk.Label(root, text="", fg='white', bg='black', font=("Helvetica", 150))
timeText.pack() 
update_timeText() 
root.mainloop() 
