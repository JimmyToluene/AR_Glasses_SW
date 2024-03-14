import main_frame
import menu_frame
import tkinter as tk

root = tk.Tk()
app = main_frame.MainFrame(root)
menu = menu_frame.MenuFrame(root)
main_frame.TimeWidget(app.main_frame)
weather_frame = main_frame.WeatherWidget(app.main_frame, "https://xml.smg.gov.mo/e_actual_brief.xml")
battery_frame = main_frame.BatteryWidget(app.main_frame)
button = main_frame.ButtonWidget(app.main_frame, menu.menu_frame)
menu_widget = menu_frame.MenuFunctionalWidget(menu.menu_frame)
menu_return_btn = main_frame.ButtonWidget(menu.menu_frame, app.main_frame)
menu_widget.creat_functional_btn()

root.mainloop()