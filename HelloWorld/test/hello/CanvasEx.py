import urllib.request
import feedparser
import tkinter as tk
import time
from datetime import date

master = tk.Tk()

w = tk.Canvas(master, width=1000, height=1000)
w.pack()
w.create_rectangle(0, 0, 1000, 1000, fill="black")
w.create_text(500, 90, text="Test", fill="white", font=("Times new roman",20))

# read weather information
weatherURL1 = 'http://weather.yahooapis.com/forecastrss?w=1132599&u=c'
response1 = urllib.request.urlopen(weatherURL1)
html1 = response1.read()

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


#w.create_text(700, 120, text=City_text, fill="white", font=("Times new roman",20), anchor = W)
#w.create_text(700, 150, text=TempLow_text, fill="white", font=("Times new roman",20), anchor = W)
#w.create_text(700, 180, text=TempHigh_text, fill="white", font=("Times new roman",20), anchor = W)
#w.create_text(700, 210, text=Humidity_text, fill="white", font=("Times new roman",20), anchor = W)

class Application(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.now = tk.StringVar()
        self.time = tk.Label(self, font=('Helvetica', 24))
        self.time.pack(side="top")
        self.time["textvariable"] = self.now

        self.QUIT = tk.Button(self, text="QUIT", fg="red",
                                            command=root.destroy)
        self.QUIT.pack(side="bottom")

        # initial time display
        self.onUpdate()

    def onUpdate(self):
        # update displayed time
        self.now.set(current_iso8601())
        # schedule timer to call myself after 1 second
        self.after(1000, self.onUpdate)

root = tk.Tk()
app = Application(master=root)
root.mainloop()

#today = date.today()
#t = today.timetuple()
#tmp_text = today.strftime("%A %d. %B %Y")
#print( tmp_text )
#time_text = time.strftime("%I:%M:%S")
#print( time_text )


w_label = w.create_text(700, 50, text=time_text, fill="white", font=("Times new roman",20), anchor = W)

label1 = tk.Label(w, textvariable=str_v)
label1.place(x=700,y=80)

#w.create_text(700, 80, textvariable = str_v, fill="white", font=("Times new roman",20), anchor = W)
    
    #time.sleep(1)
master.after(1000,change_text)
master.mainloop()