import main_frame
import menu_frame
import tkinter as tk
import navi_interface
import threading
import NavigationSub.moread
from multiprocessing import Process, Queue
def run_gui(q):
    root = tk.Tk()
    main = main_frame.MainFrame(root)
    menu = menu_frame.MenuFrame(root)
    navi = navi_interface.NaviFrame(root, q)

    main_frame.TimeWidget(main.main_frame)
    weather_frame = main_frame.WeatherWidget(main.main_frame, "https://xml.smg.gov.mo/e_actual_brief.xml")
    #battery_frame = main_frame.BatteryWidget(main.main_frame)
    button = main_frame.ButtonWidget(main.main_frame, menu.menu_frame)
    menu_widget = menu_frame.MenuFunctionalWidget(menu.menu_frame, navi.navi_frame)
    navi_return_btn = main_frame.ButtonWidget(navi.navi_frame, menu.menu_frame)
    def update_label():
        while not q.empty():
            data = q.get()  # 从队列中获取数据
            # 假设 data 是一个字典，包含了之前发送的 outcome 数据
            message = f"Speed Limit: {data['speed_limit']} km/h, Action: {data['action']}, Distance: {data['distance']}"
            label.config(text=message)  # 更新标签显示新消息
        # 重新调用自身，保持定期更新
        root.after(100, update_label)

    menu_widget.creat_functional_btn()
    menu_return_btn = main_frame.ButtonWidget(menu.menu_frame ,main.main_frame)
    root.mainloop()


def main():
    q = Queue()
    gui_process = Process(target=run_gui, args=(q,))
    ble_process = Process(target=NavigationSub.moread.main_navi, args=(q,))

    gui_process.start()
    ble_process.start()

    gui_process.join()
    ble_process.join()

if __name__ == "__main__":
    main()