import tkinter as tk
import requests
from tkinter import messagebox
from PIL import Image, ImageTk
import ttkbootstrap

def get_weather(city):
    API_key = "ab2b0cc115460e84defaf02ae2e22660"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_key}"
    res = requests.get(url)

    if res.status_code == 404:
        messagebox.showerror("Error", "City not found")
        return None
    
    weather = res.json()
    icon_id = weather['weather'][0]['icon']
    temp = weather['main']['temp']- 273.15
    description = weather['weather'][0]['description']
    city = weather['name']
    country = weather['sys']['country']

    icon_url =f"https://openweathermap.org/img/wn/{icon_id}@2x.png"
    return(icon_url, temp, description, city, country) 


def search():
    city = city_entry.get()
    result = get_weather(city)
    if result is None:
        return
    
    icon_url, temp, description, city, country = result
    location_label.configure(text=f"{city}, {country}")

    image = Image.open(requests.get(icon_url, stream=True).raw)
    icon = ImageTk.PhotoImage(image)
    icon_label.configure(image=icon)
    icon_label.image = icon

    temp_label.configure(text=f"Temperature: {temp: .2f}°C")
    descrip_label.configure(text=f"Description: {description}")


root = ttkbootstrap.Window(themename='morph')
root.title("Weather App")
root.geometry("800x600")
root.resizable(False,False)

background_frame = ttkbootstrap.Frame(root, padding=20)
background_frame.pack(fill=tk.BOTH, expand=True)

# Entry widget
city_entry = ttkbootstrap.Entry(background_frame, font="Helvetica, 16", )
city_entry.pack(pady=10)


# Button widget
search_button = ttkbootstrap.Button(background_frame, text="Search", command=search)
search_button.pack(pady=10)

#Label widget
location_label = ttkbootstrap.Label(background_frame, font="Helvetica, 22", anchor="center")
location_label.pack(pady=20)

icon_label = tk.Label(background_frame)
icon_label.pack(pady=10)

temp_label = tk.Label(background_frame, font="Helvetica, 20", anchor="center")
temp_label.pack(pady=10)

descrip_label = tk.Label(background_frame, font="Helvetica, 18", anchor="center")
descrip_label.pack(pady=10)

root.mainloop()