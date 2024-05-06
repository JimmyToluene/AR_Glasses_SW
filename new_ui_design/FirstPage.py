import tkinter as tk
import PageTwo
import functions
from time import strftime
from PIL import ImageTk, Image
import psutil


class MainFrame(tk.Frame):

    def __init__(self, parent, root):
        super().__init__(parent)

        self.bty_empty = None
        self.battery_empty = None
        self.battery_low = None
        self.bty_low = None
        self.bty_half = None
        self.battery_half = None
        self.hum_icon = None
        self.bty_more_half = None
        self.battery_more_half = None
        self.bty_charging = None
        self.battery_charging = None
        self.bty_full = None
        self.battery_full = None
        self.BatteryWidget()
        self.battery_full_label = tk.Label(self, background="black", image=self.bty_full)
        self.battery_charging_label = tk.Label(self, background="black", image=self.bty_charging)
        self.battery_more_half_label = tk.Label(self, background="black", image=self.bty_more_half)
        self.battery_half_label = tk.Label(self, background="black", image=self.bty_half)
        self.battery_low_label = tk.Label(self, background="black", image=self.bty_low)
        self.battery_empty_label = tk.Label(self, background="black", image=self.bty_empty)

        self.battery_percent_label = tk.Label(self, text="", font=("Helvetica", 25))
        self.battery_percent_label.configure(background="black")
        self.battery_percent_label.place(anchor="center", x=230, y=190)
        self.time_label = tk.Label(self, text='', font=("Helvetica", 50), bg="black")
        self.time_label.place(x=200, y=100, anchor="center")
        self.date_label = tk.Label(self, text='', font=("Helvetica", 15), bg="black", fg="white")
        self.date_label.place(x=200, y=140, anchor="center")
        self.configure(bg="black")
        self.weather_string = "https://xml.smg.gov.mo/e_actual_brief.xml"
        self.canvas = None
        self.weather_frame = None
        self.weather_widget(self.weather_string)
        self.setup_widget()
        self.update_time()
        self.battery_percent()
        self.downangle = Image.open("icon/angle/arrow_down.png")
        self.down_angle = ImageTk.PhotoImage(self.downangle.resize((32, 32)))
        self.return_btn = tk.Button(self, image=self.down_angle, command=lambda: root.show_frame(PageTwo.PageTwo))
        self.return_btn.configure(background="black")
        self.return_btn.place(anchor="center", x=320, y=370)

    def weather_widget(self, url):
        self.weather_frame = tk.Frame(self, width=200, height=170, borderwidth=5)
        self.weather_frame.configure(background="grey")
        self.weather_frame.place(x=380, y=80)

        self.canvas = tk.Canvas(self.weather_frame, width=200, height=170)
        self.canvas.configure(background="grey")
        self.canvas.pack()
        self.canvas.create_line(5, 78, 200, 78, width=1)
        self.weather_string = functions.ARGlassFunctions.getweather(url)
        self.setup_widget()

    def setup_widget(self):
        image = Image.open(functions.urllib.request.urlopen(self.weather_string[4]))
        self.weather_photo = ImageTk.PhotoImage(image)
        weather_label = tk.Label(self.weather_frame, image=self.weather_photo, bg="grey")
        weather_label.place(x=140, y=10)
        temperate_value = self.weather_string[1]  # Replace with your logic
        temperate = tk.Label(self.weather_frame, text=temperate_value, font=("Helvetica", 43), fg="white", bg="grey")
        temperate.place(x=5, y=3)

        city = tk.Label(self.weather_frame, text="Taipa, Macau", font=("Helvetica", 10), bg="grey", fg="white")
        city.place(x=10, y=60)

        updatetime = "Last update:" + self.weather_string[0].split(" ")[3]
        weather_updatetime = tk.Label(self.weather_frame, text=updatetime, font=("Helvetica", 10), bg="grey",
                                      fg="white")
        weather_updatetime.place(x=110, y=60)

        humi_icon = Image.open("/Users/jimmytoluene/AR_Glasses/icon/weather/humi_icon.png")
        self.hum_icon = ImageTk.PhotoImage(humi_icon.resize((40, 40)))
        humi_label = tk.Label(self.weather_frame, image=self.hum_icon, bg="grey")
        humi_label.place(x=5, y=85)

        humidity_value = self.weather_string[2]  # Replace with your logic
        humidity = tk.Label(self.weather_frame, text=humidity_value, font=("Helvetica", 15), fg="white", bg="grey")
        humidity.place(x=50, y=95)

        wind_icon = Image.open("/Users/jimmytoluene/AR_Glasses/icon/weather/wind_speed.png")
        self.wind_icon = ImageTk.PhotoImage(wind_icon.resize((32, 32)))
        wd_label = tk.Label(self.weather_frame, image=self.wind_icon, bg="grey")
        wd_label.place(x=6, y=135)

        wind_speed_value = self.weather_string[3]  # Replace with your logic
        wind_speed = tk.Label(self.weather_frame, text=wind_speed_value, font=("Helvetica", 15), fg="white", bg="grey")
        wind_speed.place(x=50, y=140)

    def BatteryWidget(self):
        self.battery_full = Image.open("/Users/jimmytoluene/AR_Glasses/icon/battery/battery_full.png")
        self.bty_full = ImageTk.PhotoImage(self.battery_full.resize((40, 40)))
        self.battery_charging = Image.open("/Users/jimmytoluene/AR_Glasses/icon/battery/battery_charging.png")
        self.bty_charging = ImageTk.PhotoImage(self.battery_charging.resize((40, 40)))
        self.battery_more_half = Image.open("/Users/jimmytoluene/AR_Glasses/icon/battery/battery_more_half.png")
        self.bty_more_half = ImageTk.PhotoImage(self.battery_more_half.resize((40, 40)))
        self.battery_half = Image.open("/Users/jimmytoluene/AR_Glasses/icon/battery/battery_half.png")
        self.bty_half = ImageTk.PhotoImage(self.battery_half.resize((40, 40)))
        self.battery_low = Image.open("/Users/jimmytoluene/AR_Glasses/icon/battery/battery_low.png")
        self.bty_low = ImageTk.PhotoImage(self.battery_low.resize((40, 40)))
        self.battery_empty = Image.open("/Users/jimmytoluene/AR_Glasses/icon/battery/battery_empty.png")
        self.bty_empty = ImageTk.PhotoImage(self.battery_empty.resize((40, 40)))



    def battery_percent(self):

        battery_state = psutil.sensors_battery()

        if battery_state.power_plugged:
            self.battery_charging_label.place(x=140, y=170)
        elif battery_state.percent <= 5:
            self.battery_charging_label.place_forget()
            self.battery_half_label.place_forget()
            self.battery_empty_label.place(x=140, y=170)
        elif battery_state.percent <= 25:
            self.battery_charging_label.place_forget()
            self.battery_more_half_label.place_forget()
            self.battery_low_label.place(x=140, y=170)
        elif battery_state.percent <= 50:
            self.battery_charging_label.place_forget()
            self.battery_more_half_label.place_forget()
            self.battery_half_label.place(x=140, y=170)
        elif battery_state.percent <= 75:
            self.battery_charging_label.place_forget()
            self.battery_full_label.place_forget()
            self.battery_more_half_label.place(x=140, y=170)
        elif battery_state.percent <= 100:
            self.battery_charging_label.place_forget()
            self.battery_full_label.place(x=140, y=170)
        percent_string = str(psutil.sensors_battery().percent) + "%"
        self.battery_percent_label.config(text=percent_string, fg="white")
        self.battery_percent_label.after(1000, self.battery_percent)

    def update_time(self):
        date_string = strftime("%A, %-d %B")
        time_string = strftime('%H:%M %p')
        self.time_label.config(text=time_string, fg="white")
        self.date_label.config(text=date_string)
        self.time_label.after(1000, self.update_time)
