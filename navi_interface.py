import main_frame
import tkinter as tk
from ttkbootstrap import ttk
from PIL import ImageTk, Image
from NavigationSub import moread
import threading

class NaviFrame:
    def __init__(self, root, q):
        self.number_label = None
        self.test_label = None
        self.navi_frame = None
        self.canvas = None
        self.root = root
        self.data = [0]  # 初始化数据数组
        self.create_navi_frame()
        self.create_speedlimit_display_widget()
        self.update_data_display()

    def create_navi_frame(self):
        self.navi_frame = tk.Frame(self.root, width=640, height=400)
        self.navi_frame.configure(background="black")
        self.navi_frame.pack(anchor='center', fill="both", expand=True)
        self.canvas = tk.Canvas(self.navi_frame, width=640,height=400, bg='black')
        self.canvas.pack(fill="both",expand=True)
        self.canvas.create_oval(100, 100, 300, 300, outline="red", width=10)

    def create_speedlimit_display_widget(self):
        self.number_label = tk.Label(self.navi_frame, text="", fg="white", bg="black",font=("Helvetica", 70))
        self.number_label.place(x=200, y=180, anchor="center")
        self.speed_label = tk.Label(self.navi_frame, text="Km/H", fg="white", bg="black", font=("Helvetica", 35))
        self.speed_label.place(x=200, y=250, anchor="center")

    def update_label(self, q):
        while not q.empty():
            data = q.get()
            message = f"Speed Limit: {data['speed_limit']} km/h, Action: {data['action']}, Distance: {data['distance']}"
            self.number_label.config(text=data['speed_limit'])
        self.navi_frame.after(100, self.update_label)


