import main_frame
import tkinter as tk
from ttkbootstrap import ttk
from PIL import ImageTk, Image

import menu_frame


class NaviFrame:
    def __init__(self, root, q):
        self.warning_label = None
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


    def create_information_display_widget(self):
        self.canvas = tk.Canvas(self.navi_frame, width=250, height=250, bg='black',bd=0, highlightthickness=0,relief='ridge')
        outer_circle = self.canvas.create_oval(5, 5, 150, 150, outline='red', width=10)
        inner_circle = self.canvas.create_oval(10, 10, 145, 145, fill='white', outline='')
        self.speed_limit_number = tk.Label(self.navi_frame, text="50", bg="white", font=("Helvetica", 55, 'bold'))
        self.direction_label = tk.Label(self.navi_frame, text="", fg="white", bg="black", font=("Helvetica", 27))
        self.eta_road = tk.Label(self.navi_frame, text="", fg="white", bg="black", font=("Helvetica", 33))
        self.direction_icon = tk.Label(self.navi_frame, image="", bg="black")
        self.warning_label = tk.Label(self.navi_frame, text="Device not connected",fg="white", bg="black", font=("Helvetica", 33))

    def update_information(self):
        global data
        try:
            while not self.queue.empty():
                self.warning_label.config(text="")
                data = self.queue.get_nowait()
                message = f"Speed Limit: {data['speed_limit']} km/h, Action: {data['action']}, Distance: {data['distance']}"
                if data['speed_limit'] == '0':
                    break
                else:
                    self.speed_limit_number.config(text=data['speed_limit'])
                    self.canvas.place(x=200, y=150, anchor='center')
                    self.speed_limit_number.place(x=150, y=110 ,anchor="center")
                    self.direction_icon.place(x=470, y=100, anchor="center")
                    self.eta_road.place(x=470, y=290, anchor="center")
                self.direction_label.config(text=data['action'])
                self.eta_road.config(text=data['distance'] + " left")
            try:
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
            self.warning_label.place(anchor=tk.CENTER,x=320,y=200)
            self.navi_frame.after(1000, self.update_information)
