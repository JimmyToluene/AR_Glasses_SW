# Importing tkinter module
from tkinter import *
from time import strftime
import numpy as np
import ttkbootstrap as ttk
from PIL import ImageTk, Image,ImageChops
import urllib.request
import requests
import xml.etree.ElementTree as ET
import psutil
def getweather(url):
    response = requests.get(url)
    if response.status_code == 200:
        xml_content = response.text
    else:
        print("Failed to fetch the XML data from the specified website.")
    level = 0
    root = ET.fromstring(xml_content)
    string_array = []
    for element in root.iter():
        string_array.append(f"{'    ' * level}{element.tag}: ")
        string_array.append(f"{element.text}")
    return string_array

print(getweather("https://xml.smg.gov.mo/e_actual_brief.xml"))