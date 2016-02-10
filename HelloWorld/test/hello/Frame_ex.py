# -*- coding: utf-8 -*-

import tkinter as tk 
import time
import feedparser

class Example(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)

        self.canvas = tk.Canvas(self, width=1000, height=1000, bg='black')
        self.canvas.pack(side="top", fill="both", expand=True)

        # every canvas object gets a unique id, which can be used later to change the object.
        self.text_id 		= self.canvas.create_text(500, 90, text="Test", fill="white", font=("Helvetica",20))
 
        # clock display 
        self.text_id_Day    = self.canvas.create_text(100, 50, text="00 Jan 00", fill="white", font=("Helvetica",20), anchor='nw')
        self.text_id_clock  = self.canvas.create_text(100, 80, text="00:00", fill="white", font=("Helvetica",40), anchor='nw')
        self.text_id_AmPm   = self.canvas.create_text(245, 110, text="00:00", fill="white", font=("Helvetica",15), anchor='nw')
        
        #weather display
        self.text_id_City   = self.canvas.create_text(700, 50, text="Seoul", fill="white", font=("Helvetica",15), anchor='nw')
        self.text_id_Weath  = self.canvas.create_text(700, 80, text="00 Jan 00", fill="white", font=("Helvetica",30), anchor='nw')
        
        self.on_change_text();

    def on_change_text(self):
        # Clock update
        time_str = time.localtime()
        clock_text = time.strftime("%y %b %d %H:%M:%S %p", time_str)
        self.canvas.itemconfig( self.text_id_Day,   text=time.strftime("%y %b %d", time_str))
        self.canvas.itemconfig( self.text_id_clock, text=time.strftime("%H:%M", time_str))
        self.canvas.itemconfig( self.text_id_AmPm,  text=time.strftime("%p", time_str))
        
        #Weather update
        
        # read weather information
        weatherURL1 = 'http://weather.yahooapis.com/forecastrss?w=1132599&u=c'
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
        text_weather = "H/L  "+high +"\u00b0/"+ low + "\u00b0"
        text_weather += "\nHum  " + humidity + " %"
        self.canvas.itemconfig( self.text_id_Weath,  text=text_weather)
        
        self.after(10000, self.on_change_text)
		
if __name__ == "__main__":
    root = tk.Tk()
    view = Example(root, bg='black')
    view.pack(side="top", fill="both", expand=True)
    root.mainloop()    

    
    