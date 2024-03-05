import requests
import xml.etree.ElementTree as ET

def getweather(url):
    response = requests.get(url)
    if response.status_code == 200:
        xml_content = response.text
    else:
        print("Failed to fetch the XML data from the specified website.")
        return None

    root = ET.fromstring(xml_content)
    string_array = []

    sys_pubdate = root.find(".//SysPubdate")
    if sys_pubdate is not None:
        string_array.append(f"Update time: {sys_pubdate.text}")

    temperature = root.find(".//Temperature")
    if temperature is not None:
        temp_string = f"{temperature.find('Value').text} °C"
        string_array.append(temp_string)

    humidity = root.find(".//Humidity")
    if humidity is not None:
        humidity_string = f"Humidity: {humidity.find('Value').text}%"
        string_array.append(humidity_string)

    wind_speed = root.find(".//WindSpeed")
    if wind_speed is not None:
        wind_speed_string = f"Wind speed: {wind_speed.find('Value').text} km/h"
        string_array.append(wind_speed_string)

    icon = root.find(".//Icon")
    if icon is not None:
        icon_url = icon.find('IconURL').text
        string_array.append(icon_url)

    return string_array

url = "https://xml.smg.gov.mo/e_actual_brief.xml"
print(getweather(url))

