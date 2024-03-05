# Importing tkinter module
from tkinter import *
from time import strftime
import ttkbootstrap as ttk
from PIL import ImageTk, Image, ImageChops
import urllib.request
import requests
import xml.etree.ElementTree as ET
import psutil


def getweather(url):
    response = requests.get(url)
    if response.status_code == 200:
        xml_content = response.text
    else:
        print("Failed to fetch the XML data from the specified website.")
    level = 0
    root = ET.fromstring(xml_content)
    string_array = []
    for element in root.iter():
        string_array.append(f"{'    ' * level}{element.tag}: ")
        string_array.append(f"{element.text}")
    return string_array

def time():
    date_string = strftime("%A,%-d %B")
    time_string = strftime('%H:%M %p')
    time_label.config(text=time_string, fg="white")
    date_label.config(text=date_string)
    time_label.after(1000, time)

def battery_percent():
    battery_state = psutil.sensors_battery()
    if battery_state.power_plugged:
        battery_charging_label.place(x=140, y=170)
    if (battery_state.percent <= 100) and (battery_state.power_plugged == 0):
        battery_charging_label.place_forget()
        battery_full_label.place(x=140, y=170)

    percent_string = str(psutil.sensors_battery().percent) + "%"
    battery_percent_label.config(text=percent_string, fg="white")
    battery_percent_label.after(100, battery_percent)


#Main window
root = ttk.Window()
root.geometry("640x400")
root.configure(bg='black')

#Main frame
main_frame = Frame(root, width=640, height=400)
main_frame.configure(bg="black")
main_frame.pack(anchor='center', fill="both", expand=False)
menu_frame = Frame(root, width=640, height=400)  # This is Menu Frame


time_label = Label(main_frame, text='', font=("Helvetica", 50))
time_label.configure(background="black")
time_label.place(x=200, y=100, anchor="center")
date_label = Label(main_frame, text='', font=("Helvetica", 15))
date_label.configure(background="black", fg="white")
date_label.place(x=200, y=140, anchor="center")
time()

battery_full = Image.open("../icon/battery/battery_full.png")
bty_full = ImageTk.PhotoImage(battery_full.resize((40, 40)))
battery_charging = Image.open("../icon/battery/battery_charging.png")
bty_charging = ImageTk.PhotoImage(battery_charging.resize((40, 40)))

battery_full_label = ttk.Label(main_frame, background="black", image=bty_full)
battery_charging_label = ttk.Label(main_frame, background="black", image=bty_charging)
battery_percent_label = Label(main_frame, text="", font=("Helvetica", 25))
battery_percent_label.configure(background="black")
battery_percent_label.place(anchor="center", x=230, y=190)
battery_percent()


weather_frame = Frame(main_frame, width=200, height=170, borderwidth=5)
weather_frame.configure(background="grey")
weather_frame.place(x=380, y=80)
canvas = Canvas(weather_frame, width=200, height=170)
canvas.configure(background="grey")
canvas.pack()
canvas.create_line(10, 78, 190, 78, width=1)



image = Image.open(urllib.request.urlopen('https://www.smg.gov.mo/icons/weatherIcon/ww-c13.gif'))
photo = ImageTk.PhotoImage(image)
string_array = getweather("https://xml.smg.gov.mo/e_actual_brief.xml")
humi_icon = Image.open("../icon/weather/humi_icon.png")
hum_icon = ImageTk.PhotoImage(humi_icon.resize((40, 40)))
wind_icon = Image.open("../icon/weather/wind_speed.png")
wind_icon = ImageTk.PhotoImage(wind_icon.resize((32, 32)))
weather_label = ttk.Label(weather_frame, image=photo, background="grey")
weather_label.place(x=140, y=5)
temperate_value = string_array[21] + '°C'
temperate = Label(weather_frame, text=temperate_value, font=("Helvetica", 43), fg="white")
temperate.configure(background="grey", fg="white")
temperate.place(x=5, y=3)
city = Label(weather_frame, text="Taipa,Macau", font=("Helvetica", 10))
city.configure(background="grey", fg="white")
city.place(x=10, y=60)
string_updatetime = string_array[7].split()
weather_updatetime = Label(weather_frame, text="Last update:"+string_updatetime[1], font=("Helvetica", 10))
weather_updatetime.configure(background="grey", fg="white")
weather_updatetime.place(x=100, y=60)
humi_label = ttk.Label(weather_frame, image=hum_icon, background="grey")
humi_label.place(x=5, y=85)
humi_value = "Humidity: " + string_array[29] + '%'
humidity = Label(weather_frame, text=humi_value, font=("Helvetica", 15), background="black")
humidity.configure(background="grey", fg="white")
humidity.place(x=50, y=95)
wd_label = ttk.Label(weather_frame, image=wind_icon, background="grey")
wd_label.place(x=6, y=135)
wd_value = "WindSpeed: " + string_array[37] + string_array[33]
wind_speed = Label(weather_frame, text=wd_value, font=("Helvetica", 15), background="black")
wind_speed.configure(background="grey", fg="white")
wind_speed.place(x=50, y=140)



menu_frame = Frame(root, width=640, height=400, bg="black")  # This is Menu Frame
def raise_memu():
    main_frame.pack_forget()
    menu_frame.configure(bg="black")
    menu_frame.pack(anchor='center', fill="both", expand=False)

down_angle = Image.open("../icon/angle/arrow_down.png")
down_angle = ImageTk.PhotoImage(down_angle.resize((32, 32)))

#设置按钮的背景颜色
style = ttk.Style()
style.configure("BW.TLabel", background="black")

#为main_frame和menu_frame防止
btn = ttk.Button(main_frame, style="BW.TLabel", image=down_angle, command=raise_memu)
btn.place(anchor="center", x=320, y=370)
btn = ttk.Button(menu_frame, style="BW.TLabel", image=down_angle, command=raise_memu)
btn.place(anchor="center", x=320, y=370)

menu_frame_label = Frame(menu_frame,width=400,height=200)
menu_frame_label.configure(background="black")
menu_frame_label.place(anchor=CENTER,x=320,y=200)

map_icon = ImageTk.PhotoImage(Image.open("../icon/menu_icon/map.png"))
map_btn = ttk.Button(menu_frame_label, style="BW.TLabel",image=map_icon)
map_btn.place(anchor="center", x=50, y=100)

camera_icon = ImageTk.PhotoImage(Image.open("../icon/menu_icon/camera.png"))
camera_icon_btn = ttk.Button(menu_frame_label, style="BW.TLabel", image=camera_icon)
camera_icon_btn.place(anchor="center", x=140, y=100)

voice_icon = ImageTk.PhotoImage(Image.open("../icon/menu_icon/microphone.png"))
camera_icon_btn = ttk.Button(menu_frame_label, style="BW.TLabel", image=voice_icon)
camera_icon_btn.place(anchor="center", x=230, y=100)

mail_icon = ImageTk.PhotoImage(Image.open("../icon/menu_icon/mail-xl.png"))
mail_icon_btn = ttk.Button(menu_frame_label, style="BW.TLabel", image=mail_icon)
mail_icon_btn.place(anchor="center", x=310, y=100)

ai_icon = ImageTk.PhotoImage(Image.open("../icon/menu_icon/robot.png"))
ai_icon_btn = ttk.Button(menu_frame_label, style="BW.TLabel", image=ai_icon)
ai_icon_btn.place(anchor="center", x=410, y=100)
root.mainloop()
