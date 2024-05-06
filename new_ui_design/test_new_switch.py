import FirstPage
import PageTwo
import PageFive
import tkinter as tk
import PageThree
from multiprocessing import Queue,Process

q = Queue()
class Application(tk.Tk):
    def __init__(self, q):
        super().__init__()
        self.q = q
        self.geometry("640x400")
        self.configure(bg='black')
        self.wm_title("AR Glasses Interface")
        container = tk.Frame(self)
        container.configure(bg="black")
        container.pack(side="top", fill="both", expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        self.frames = {}
        for F in (FirstPage.MainFrame, PageTwo.PageTwo, PageThree.PageThree,PageFive.PageFive):
            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage.MainFrame)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


if __name__ == '__main__':
    # 实例化Application
    app = Application(q)
    app.mainloop()
