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
        self.canvas.create_oval(80, 80, 280, 280, outline="red", width=10)

    def create_information_display_widget(self):
        self.speed_limit_number = tk.Label(self.navi_frame, text="", fg="white", bg="black",font=("Helvetica", 70))
        self.speed_limit_number.place(x=180, y=170, anchor="center")
        self.speed_limit_tag_label = tk.Label(self.navi_frame, text="Km/H", fg="white", bg="black", font=("Helvetica", 35))
        self.speed_limit_tag_label.place(x=180, y=230, anchor="center")
        self.direction_label = tk.Label(self.navi_frame, text="", fg="white", bg="black",font=("Helvetica", 27))
        self.direction_label.place(x=470, y=240, anchor="center")
        self.eta_road = tk.Label(self.navi_frame, text="", fg="white", bg="black",font=("Helvetica", 33))
        self.eta_road.place(x=470, y=290, anchor="center")
        self.direction_icon = tk.Label(self.navi_frame, image="", bg="black")
        self.direction_icon.place(x=470, y=100, anchor="center")

    def update_information(self):
        global data
        try:
            while not self.queue.empty():
                data = self.queue.get_nowait()
                message = f"Speed Limit: {data['speed_limit']} km/h, Action: {data['action']}, Distance: {data['distance']}"
                self.speed_limit_number.config(text=data['speed_limit'])
                self.direction_label.config(text=data['action'])
                self.eta_road.config(text=data['distance'])
            try :
                file_name = f"./icon/navi_icon/png/{data['direction_code']}.png"
                img = Image.open(file_name)
                photo = ImageTk.PhotoImage(img)
                self.direction_icon.config(image=photo)
                self.direction_icon.image = photo
            except Exception as e:
                print(f"An error occurred: {e}")
            self.navi_frame.after(500, self.update_information)
        except Exception as e:
            print(f"An error occurred: {e}")

