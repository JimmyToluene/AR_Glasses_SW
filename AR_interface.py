import main_frame
import menu_frame
import tkinter as tk
import navi_interface
import threading
import NavigationSub.moread
from multiprocessing import Process, Queue
def run_gui():
    root = tk.Tk()
    main = main_frame.MainFrame(root)
    menu = menu_frame.MenuFrame(root)
    navi = navi_interface.NaviFrame(root)

    main_frame.TimeWidget(main.main_frame)
    weather_frame = main_frame.WeatherWidget(main.main_frame, "https://xml.smg.gov.mo/e_actual_brief.xml")
    battery_frame = main_frame.BatteryWidget(main.main_frame)
    button = main_frame.ButtonWidget(main.main_frame, menu.menu_frame)
    menu_widget = menu_frame.MenuFunctionalWidget(menu.menu_frame, navi.navi_frame)
    navi_return_btn = main_frame.ButtonWidget(navi.navi_frame, menu.menu_frame)
    menu_widget.creat_functional_btn()
    menu_return_btn = main_frame.ButtonWidget(menu.menu_frame ,main.main_frame)
    root.mainloop()


def main():
    q = Queue()

    # 创建 GUI 进程
    gui_process = Process(target=run_gui, args=(q,))

    # 创建 BLE 服务进程
    ble_process = Process(target=NavigationSub.moread.main_navi, args=(q,))

    # 启动进程
    gui_process.start()
    ble_process.start()

    # 等待进程完成
    gui_process.join()
    ble_process.join()

if __name__ == "__main__":
    main()