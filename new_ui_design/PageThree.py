import tkinter as tk
from PIL import ImageTk, Image
import PageTwo
import test_new_switch


class PageThree(tk.Frame):
    def __init__(self,parent,root):
        super().__init__(parent)
        self.queue = test_new_switch.q
        self.config(bg="black")
        self.warning_label = None
        self.direction_icon = None
        self.eta_road = None
        self.direction_label = None
        self.speed_limit_tag_label = None
        self.speed_limit_number = None
        self.navi_frame = None
        self.canvas = None
        self.root = root
        self.data = [0]  # 初始化数据数组
        self.create_information_display_widget()
        self.update_information()

        self.downangle = Image.open("icon/angle/arrow_down.png")
        self.down_angle = ImageTk.PhotoImage(self.downangle.resize((32, 32)))
        self.return_btn = tk.Button(self, image=self.down_angle, command=lambda:root.show_frame(PageTwo.PageTwo))
        self.return_btn.configure(background="black")
        self.return_btn.place(anchor="center", x=320, y=370)



    def create_information_display_widget(self):
        self.canvas = tk.Canvas(self, width=250, height=250, bg='black',bd=0, highlightthickness=0,relief='ridge')
        outer_circle = self.canvas.create_oval(5, 5, 150, 150, outline='red', width=10)
        inner_circle = self.canvas.create_oval(10, 10, 145, 145, fill='white', outline='')
        self.speed_limit_number = tk.Label(self, text="50", bg="white", font=("Helvetica", 55, 'bold'))
        self.direction_label = tk.Label(self, text="", fg="white", bg="black", font=("Helvetica", 27))
        self.eta_road = tk.Label(self, text="", fg="white", bg="black", font=("Helvetica", 33))
        self.direction_icon = tk.Label(self, image="", bg="black")

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
            self.warning_label = tk.Label(self, text="Device not connected", fg="white", bg="black",
                                          font=("Helvetica", 33))
            self.warning_label.place(anchor=tk.CENTER,x=320,y=200)
            self.after(1000, self.update_information)

