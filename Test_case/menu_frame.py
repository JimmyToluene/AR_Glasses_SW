import main_frame
import tkinter as tk
from ttkbootstrap import ttk
from PIL import ImageTk, Image


class MenuFrame:
    def __init__(self, root):
        self.menu_frame = None
        self.root = root
        self.create_menu_frame()

    def create_menu_frame(self):
        self.menu_frame = tk.Frame(self.root, width=640, height=400)
        self.menu_frame.configure(background="black")
        self.menu_frame.pack(anchor='center', fill="both", expand=False)


class MenuFunctionalWidget:
    def __init__(self, master, new_frame):
        self.new_frame = new_frame
        self.master = master
        self.window = None
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
        self.map_icon = ImageTk.PhotoImage(Image.open("../icon/menu_icon/map.png"))
        self.map_btn = tk.Button(self.label, image=self.map_icon,command=self.map_button)
        self.map_btn.place(anchor="center", x=100, y=100)

        self.camera_icon = ImageTk.PhotoImage(Image.open("../icon/menu_icon/instagram-64.png"))
        self.camera_icon_btn = tk.Button(self.label, image=self.camera_icon)
        self.camera_icon_btn.place(anchor="center", x=200, y=100)

        self.voice_icon = ImageTk.PhotoImage(Image.open("../icon/menu_icon/microphone.png"))
        self.voice_icon_btn = tk.Button(self.label, image=self.voice_icon)
        self.voice_icon_btn.place(anchor="center", x=300, y=100)

        self.mail_icon = ImageTk.PhotoImage(Image.open("../icon/menu_icon/mail-3-64.png"))
        self.mail_icon_btn = tk.Button(self.label, image=self.mail_icon)
        self.mail_icon_btn.place(anchor="center", x=400, y=100)

        self.ai_icon = ImageTk.PhotoImage(Image.open("../icon/menu_icon/assistant-64.png"))
        self.ai_icon_btn = tk.Button(self.label, image=self.ai_icon)
        self.ai_icon_btn.place(anchor="center", x=500, y=100)

    def map_button(self):
        self.master.pack_forget()
        self.new_frame.configure(bg="black")
        self.new_frame.pack(anchor='center', fill="both", expand=False)

