import FirstPage
import tkinter as tk
from ttkbootstrap import ttk
from PIL import ImageTk, Image

import PageThree
import PageFive


class PageTwo(tk.Frame):
    def __init__(self, parent, root):
        super().__init__(parent)
        self.configure(bg="black")
        self.widget = MenuFunctionalWidget(self)
        self.widget.creat_functional_btn(root)
        self.downangle = Image.open("icon/angle/arrow_down.png")
        self.down_angle = ImageTk.PhotoImage(self.downangle.resize((32, 32)))
        self.return_btn = tk.Button(self, image=self.down_angle, command=lambda: root.show_frame(FirstPage.MainFrame))
        self.return_btn.configure(background="black")
        self.return_btn.place(anchor="center", x=320, y=370)


class MenuFunctionalWidget:
    def __init__(self, master):
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

    def creat_functional_btn(self, root):
        self.style = ttk.Style()
        self.style.configure("BW.TLabel", background="black")
        self.map_icon = ImageTk.PhotoImage(Image.open("icon/menu_icon/map.png"))
        self.map_btn = tk.Button(self.label, image=self.map_icon, command=lambda :root.show_frame(PageThree.PageThree))
        self.map_btn.place(anchor="center", x=100, y=100)

        self.camera_icon = ImageTk.PhotoImage(Image.open("icon/menu_icon/instagram-64.png"))
        self.camera_icon_btn = tk.Button(self.label, image=self.camera_icon)
        self.camera_icon_btn.place(anchor="center", x=200, y=100)

        self.voice_icon = ImageTk.PhotoImage(Image.open("icon/menu_icon/microphone.png"))
        self.voice_icon_btn = tk.Button(self.label, image=self.voice_icon,command = lambda :root.show_frame(PageFive.PageFive))
        self.voice_icon_btn.place(anchor="center", x=300, y=100)

        self.mail_icon = ImageTk.PhotoImage(Image.open("icon/menu_icon/mail-3-64.png"))
        self.mail_icon_btn = tk.Button(self.label, image=self.mail_icon)
        self.mail_icon_btn.place(anchor="center", x=400, y=100)

        self.ai_icon = ImageTk.PhotoImage(Image.open("icon/menu_icon/assistant-64.png"))
        self.ai_icon_btn = tk.Button(self.label, image=self.ai_icon)
        self.ai_icon_btn.place(anchor="center", x=500, y=100)

