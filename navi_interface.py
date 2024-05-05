import main_frame
import tkinter as tk
from ttkbootstrap import ttk
from PIL import ImageTk, Image
from NavigationSub import moread
import threading

class NaviFrame:
    def __init__(self, root, q):
        self.direction_icon = None
        self.eta_road = None
        self.direction_label = None
        self.speed_limit_tag_label = None
        self.speed_limit_number = None
        self.queue = q
        self.navi_frame = None
        self.canvas = None
        self.root = root
        self.data = [0]  # 初始化数据数组
        self.create_navi_frame()
        self.create_information_display_widget()
        self.update_information()

    def create_navi_frame(self):
        self.navi_frame = tk.Frame(self.root, width=640, height=400)
        self.navi_frame.configure(background="black")
        self.navi_frame.pack(anchor='center', fill="both", expand=True)
        self.canvas = tk.Canvas(self.navi_frame, width=640,height=400, bg='black')
        self.canvas.pack(fill="both",expand=True)
        self.canvas.create_oval(100, 100, 300, 300, outline="red", width=10)

    def create_information_display_widget(self):
        self.speed_limit_number = tk.Label(self.navi_frame, text="", fg="white", bg="black",font=("Helvetica", 70))
        self.speed_limit_number.place(x=200, y=180, anchor="center")
        self.speed_limit_tag_label = tk.Label(self.navi_frame, text="Km/H", fg="white", bg="black", font=("Helvetica", 35))
        self.speed_limit_tag_label.place(x=200, y=250, anchor="center")
        self.direction_label = tk.Label(self.navi_frame, text="", fg="white", bg="black",font=("Helvetica", 35))
        self.direction_label.place(x=500, y=270, anchor="center")
        self.eta_road = tk.Label(self.navi_frame, text="", fg="white", bg="black",font=("Helvetica", 30))
        self.eta_road.place(x=500, y=300, anchor="center")
        self.direction_icon = tk.Label(self.navi_frame, image="", fg="white", bg="black",font=("Helvetica", 35))
        self.direction_icon.place(x=500, y=50, anchor="center")

    def update_information(self):
        try:
            while not self.queue.empty():
                data = self.queue.get_nowait()
                message = f"Speed Limit: {data['speed_limit']} km/h, Action: {data['action']}, Distance: {data['distance']}"
                self.speed_limit_number.config(text=data['speed_limit'])
                self.direction_label.config(text=data['action'])
                self.eta_road.config(text=data['distance'])
                file_name = f"./icon/navi_icon/png/{data['direction_code']}.png"
                img = Image.open(file_name)
                img = img.resize((24, 24))
                photo = ImageTk.PhotoImage(img)
                self.direction_icon.image = img
                self.direction_icon.config(image=photo)
            self.navi_frame.after(500, self.update_information)
        except Exception as e:
            print(f"An error occurred: {e}")

