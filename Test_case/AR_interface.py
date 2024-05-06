import main_frame
import menu_frame
import tkinter as tk
import navi_interface
from multiprocessing import Process, Queue



def run_gui(q):
    root = tk.Tk()
    root.attributes('-fullscreen', False)

    main = main_frame.MainFrame(root)
    menu = menu_frame.MenuFrame(root)
    navi = navi_interface.NaviFrame(root, q)

    def on_escape(event=None):
        root.attributes('-fullscreen', False)

    root.bind('<Escape>', on_escape)

    main_frame.TimeWidget(main.main_frame)
    weather_frame = main_frame.WeatherWidget(main.main_frame, "https://xml.smg.gov.mo/e_actual_brief.xml")
    battery_frame = main_frame.BatteryWidget(main.main_frame)
    button = main_frame.ButtonWidget(main.main_frame, menu.menu_frame)

    menu_widget = menu_frame.MenuFunctionalWidget(menu.menu_frame, navi.navi_frame)
    navi_return_btn = main_frame.ButtonWidget(navi.navi_frame, menu.menu_frame)

    menu_widget.creat_functional_btn()
    menu_return_btn = main_frame.ButtonWidget(menu.menu_frame, main.main_frame)
    root.mainloop()


def main():
    q = Queue()
    gui_process = Process(target=run_gui, args=(q,))
    ble_process = Process(target=NavigationSub.moread.main_navi, args=(q,))

    gui_process.start()
    ble_process.start()

    gui_process.join()
    ble_process.join()


try:
    import NavigationSub.moread
    if __name__ == "__main__":
        main()
except:
    q = Queue
    run_gui(q)

