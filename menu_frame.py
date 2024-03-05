import main_frame
import tkinter as tk
from ttkbootstrap import ttk
from PIL import ImageTk, Image



class MenuFrame:
    def __init__(self, root):
        self.menu_frame = None
        self.root = root
        self.create_main_frame()

    def create_main_frame(self):
        self.menu_frame = tk.Frame(self.root, width=640, height=400)
        self.menu_frame.configure(background="black")
        self.menu_frame.pack(anchor='center', fill="both", expand=False)


class MenuFunctionalWidget:
    def __init__(self, master):
        self.style = None
        self.ai_icon_btn = None
        self.ai_icon = None
        self.mail_icon_btn = None
        self.mail_icon = None
        self.voice_icon_btn = None
        self.camera_icon_btn = None
        self.voice_icon = None
        self.camera_icon = None
        self.map_btn = None
        self.map_icon = None
        self.label = tk.Frame(master, width=600, height=200)
        self.label.configure(background="black")
        self.label.place(anchor="center", x=320, y=200)
    def creat_functional_btn(self):
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", background="black")
        self.map_icon = ImageTk.PhotoImage(Image.open("icon/menu_icon/map.png"))
        self.map_btn = tk.Button(self.label, image=self.map_icon, background="grey")
        self.map_btn.configure(background="grey")
        self.map_btn.place(anchor="center", x=100, y=100)

        self.camera_icon = ImageTk.PhotoImage(Image.open("icon/menu_icon/camera.png"))
        self.camera_icon_btn = tk.Button(self.label, image=self.camera_icon)
        self.camera_icon_btn.place(anchor="center", x=200, y=100)

        self.voice_icon = ImageTk.PhotoImage(Image.open("icon/menu_icon/microphone.png"))
        self.voice_icon_btn = tk.Button(self.label, image=self.voice_icon)
        self.voice_icon_btn.place(anchor="center", x=300, y=100)

        self.mail_icon = ImageTk.PhotoImage(Image.open("icon/menu_icon/mail-xl.png"))
        self.mail_icon_btn = tk.Button(self.label, image=self.mail_icon)
        self.mail_icon_btn.place(anchor="center", x=400, y=100)

        self.ai_icon = ImageTk.PhotoImage(Image.open("icon/menu_icon/robot.png"))
        self.ai_icon_btn = tk.Button(self.label, image=self.ai_icon)
        self.ai_icon_btn.place(anchor="center", x=500, y=100)

root = tk.Tk()
app = main_frame.MainFrame(root)
menu = MenuFrame(root)
main_frame.TimeWidget(app.main_frame)
weather_frame = main_frame.WeatherWidget(app.main_frame, "https://xml.smg.gov.mo/e_actual_brief.xml")
battery_frame = main_frame.BatteryWidget(app.main_frame)
button = main_frame.ButtonWidget(app.main_frame, menu.menu_frame)
menu_widget = MenuFunctionalWidget(menu.menu_frame)
menu_return_btn = main_frame.ButtonWidget(menu.menu_frame,app.main_frame)
menu_widget.creat_functional_btn()

root.mainloop()
