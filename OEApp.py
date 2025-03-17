#import library
import tkinter as tk
import webbrowser
import os
import requests
from tkinter import messagebox
from dotenv import load_dotenv
import tkintermapview
#Don't touch, it's for environment variables
load_dotenv()
API_KEY = os.getenv('API_KEY')
OPEN_WEATHER_URL = os.getenv('BASE_URL_WEATHER')
OPEN_GEOCODING_URL = os.getenv('BASE_URL_GEOCODING')
#Global variable
options = ["Brampton", "Toronto", "Mississauga", "Etobicoke", "North York", "Vaughan", "Sault Ste. Marie"]

def init():
    #Don't touch if you doesn't know what it does, left it as is !
    #Init window
    root = tk.Tk()
    root.geometry('720x550')
    root.maxsize(720,550)
    root.title("Ontario Emergency App")
    #Init container
    container = tk.Frame(root)
    container.pack(fill="both", expand=True)
    container.grid_rowconfigure(0, weight=1)
    container.grid_columnconfigure(0, weight=1)
    #Init Frames
    frames ={
        "home" : tk.Frame(container),
        "call911" : tk.Frame(container),
        "call511" : tk.Frame(container),
        "callfd" : tk.Frame(container),
        "wildfire" : tk.Frame(container),
        "weather" : tk.Frame(container),
        "map" : tk.Frame(container),
        "evacuation" : tk.Frame(container),
        "about" : tk.Frame(container)
    }
    #Frame stack settings
    for frame in frames.values():
        frame.grid(row=0, column=0, sticky="nsew")
    #Setup frame
    set_home_frame(frames["home"])
    set_511_frame(frames["call511"])
    set_911_frame(frames["call911"])
    set_about_frame(frames["about"])
    set_evacuation_frame(frames["evacuation"])
    set_fd_frame(frames["callfd"])
    set_map_frame(frames["map"])
    set_weather_frame(frames["weather"])
    set_wildfire_frame(frames["wildfire"])
    #Init Menu bar widget
    menu_bar = tk.Menu(root)
    #Cascade menu
    emergency_menu = tk.Menu(menu_bar, tearoff=0)
    emergency_menu.add_command(label = "Call 911", command = lambda: show_frame(frames["call911"]))
    emergency_menu.add_command(label = "Call fire departement",  command= lambda: show_frame(frames["callfd"]))
    emergency_menu.add_command(label = "Call 511",  command =  lambda: show_frame(frames["call511"]))
    menu_bar.add_cascade(label = "Emergency Contact", menu = emergency_menu)
    #Standalone menu
    menu_bar.add_command(label = "Wild fire alerts", command = lambda: show_frame(frames["wildfire"]))
    menu_bar.add_command(label = "Weather updates", command = lambda: show_frame(frames["weather"]))
    menu_bar.add_command(label = "Interactive map", command = lambda: show_frame(frames["map"]))
    menu_bar.add_command(label = "Evacuation estimation", command = lambda: show_frame(frames["evacuation"]))
    menu_bar.add_command(label = "About", command = lambda: show_frame(frames["about"]))
    #Display Widget
    root.config(menu=menu_bar)
    show_frame(frames["home"])
    root.mainloop()

def set_home_frame(frame):
    #Welcome frame
    label_welcome = tk.Label(frame, text="Welcome to Ontario Emergency App \n OEApp", font=("Arial 20"))
    label_welcome.place(relx=0.5, rely=0.5, anchor="center")

def set_911_frame(frame):
    #Call 911 frames
    label_911 = tk.Label(frame, text="Call 911", font=("Arial 20"), cursor="hand2", fg="red")
    def on_click_phone(e):
        label_911.config(fg="darkblue")
        try:
            webbrowser.open("tel:911")
        except Exception as ex:
            frame.clipboard_clear()
            frame.clipboard_append("911")
            show_toast(frame.winfo_toplevel(), "Number copid to clipboard !")
        label_911.after(200, lambda: label_911.config(fg="blue"))

    label_911.bind("<Button-1>", on_click_phone)
    label_911.bind("<Enter>", lambda e: label_911.config(fg="darkblue"))
    label_911.bind("<Leave>", lambda e: label_911.config(fg="blue"))
    label_911.pack(pady=20)


def set_511_frame(frame):
    #Call 511 frames
    label_511 = tk.Label(frame, text="Call 511", font=("Arial 20"), cursor="hand2", fg="red")
    def on_click_phone(e):
        label_511.config(fg="darkblue")
        try:
            webbrowser.open("tel:511")
        except Exception as ex:
            frame.clipboard_clear()
            frame.clipboard_append("511")
            show_toast(frame.winfo_toplevel(), "Number copid to clipboard !")
        label_511.after(200, lambda: label_511.config(fg="blue"))

    label_511.bind("<Button-1>", on_click_phone)
    label_511.bind("<Enter>", lambda e: label_511.config(fg="darkblue"))
    label_511.bind("<Leave>", lambda e: label_511.config(fg="blue"))
    label_511.pack(pady=20)

def set_fd_frame(frame):
    #Call fire dept frames
    label_fd = tk.Label(frame, text="Call Fire department", font=("Arial 20"), cursor="hand2", fg="red")
    def on_click_phone(e):
        label_fd.config(fg="darkblue")
        try:
            webbrowser.open("tel:+19054533311")
        except Exception as ex:
            frame.clipboard_clear()
            frame.clipboard_append("+19054533311")
            show_toast(frame.winfo_toplevel(), "Number copid to clipboard !")
        label_fd.after(200, lambda: label_fd.config(fg="blue"))

    label_fd.bind("<Button-1>", on_click_phone)
    label_fd.bind("<Enter>", lambda e: label_fd.config(fg="darkblue"))
    label_fd.bind("<Leave>", lambda e: label_fd.config(fg="blue"))
    label_fd.pack(pady=20)

def set_map_frame(frame):
    # Initialize the map widget
    map_widget = tkintermapview.TkinterMapView(frame, width=700, height=500, corner_radius=0)
    map_widget.pack(pady=10)

    # Set the default location (e.g., Ontario, Canada) and zoom level
    map_widget.set_position(51.2538, -85.3232)  # Coordinates for Ontario
    map_widget.set_zoom(6)

    locations = {
        "Brampton": (43.7315, -79.7624),
        "Toronto": (43.651070, -79.347015),
        "Mississauga": (43.5890, -79.6441),
        "Etobicoke": (43.6542, -79.5671),
        "North York": (43.7615, -79.4111),
        "Vaughan": (43.8563, -79.5085),
        "Sault Ste. Marie": (46.5219, -84.3461)
    }

    # Add markers for each location
    for city, (lat, lon) in locations.items():
        map_widget.set_marker(lat, lon, text=city)

def set_weather_frame(frame):
    #Get weather update
    selected_city = tk.StringVar(frame)
    selected_city.set(options[0])
    city_label = tk.Label(frame, text="Enter City: ", font=("Arial 15"))
    city_label.pack(pady=20)

    city_dropdown = tk.OptionMenu(frame, selected_city , *options)
    city_dropdown.config(font=("Arial 15"))
    city_dropdown.pack(pady=10)

    city_dsp_label = tk.Label(frame, text="City: ", font=("Arial 15"))
    city_dsp_label.pack(pady=10)

    temp_label = tk.Label(frame, text="Temperature: ", font=("Arial 15"))
    temp_label.pack(pady=10)

    feel_label = tk.Label(frame, text="Feels like: ", font=("Arial 15"))
    feel_label.pack(pady=10)

    humid_label = tk.Label(frame, text="Humidity: ", font=("Arial 15"))
    humid_label.pack(pady=10)

    weather_label = tk.Label(frame, text="Weather: ", font=("Arial, 15"))
    weather_label.pack(pady=10)

    wind_label =  tk.Label(frame, text="Wind speed: ", font=("Arial 15"))
    wind_label.pack(pady=10)

    def update_weather():
        city = selected_city.get()
        if not city:
            messagebox.showwarning("Input error", "Please enter a cinty name")
            return
        
        weather_data = fetch_weather(city)
        if weather_data:
            city_dsp_label.config(text=f"City: {weather_data['city']}")
            temp_label.config(text=f"Temperature: {weather_data['temperature']}°C")
            feel_label.config(text=f"Feels sike: {weather_data['feels_like']}")
            humid_label.config(text=f"Humidity: {weather_data['humidity']}%")
            weather_label.config(text=f"Weather: {weather_data['weather']}")
            wind_label.config(text=f"Wind speed: {weather_data['wind_speed']} m/s")

    get_button = tk.Button(frame, text="Get Weather", command=update_weather, font=("Arial 15"))
    get_button.pack(pady=20)



def set_wildfire_frame(frame):
    #Get wildfire alert
    

    # Wildfire alert frame
    label_wildfire = tk.Label(frame, text="", font=("Arial", 20), fg="red")
    label_wildfire.pack(pady=10)
    
    button_wildfire = tk.Button(frame, text="View Wildfire Alerts", font=("Arial", 15), fg="white", bg="red", cursor="hand2",
                                command=lambda: webbrowser.open("https://www.ontario.ca/page/forest-fires"))
    button_wildfire.pack(pady=20)


def set_evacuation_frame(frame):
    label_title = tk.Label(frame, text="Evacuation Estimation", font=("Arial", 20), fg="red")
    label_title.pack(pady=20)

    label_population = tk.Label(frame, text="Estimated Population:", font=("Arial", 15))
    label_population.pack()
    entry_population = tk.Entry(frame, font=("Arial", 15))
    entry_population.pack(pady=10)

    label_routes = tk.Label(frame, text="Available Exit Routes:", font=("Arial", 15))
    label_routes.pack()
    entry_routes = tk.Entry(frame, font=("Arial", 15))
    entry_routes.pack(pady=10)

    result_label = tk.Label(frame, text="", font=("Arial", 15), fg="blue")
    result_label.pack(pady=10)

    def calculate_evacuation():
        try:
            population = int(entry_population.get())
            routes = int(entry_routes.get())
            if population <= 0 or routes <= 0:
                result_label.config(text="Please enter valid numbers.")
                return

            avg_speed = 1.2  # Average walking speed in m/s
            route_capacity = 500  # Average people per exit per minute
            estimated_time = (population / (routes * route_capacity)) * 60  # in minutes

            result_label.config(text=f"Estimated Evacuation Time: {estimated_time:.2f} minutes")
        except ValueError:
            result_label.config(text="Invalid input! Enter numbers only.")

    btn_calculate = tk.Button(frame, text="Calculate Time", command=calculate_evacuation, font=("Arial", 15))
    btn_calculate.pack(pady=10)
    pass

def set_about_frame(frame):
    #About frame
    pass

def show_frame(frame):
    #Handle change frame function
    frame.lift()

def show_toast(root, message):
    toast = tk.Label(root, text=message, bg="black", fg="white", font=("Arial", 10))
    toast.pack(side="buttom", fill="x", pady=10)
    toast.after(2000, toast.destroy)

def fetch_weather(city):
    try:
        params_geocoding = {"q": str(city) + ",CA", "appid": API_KEY}
        res_geocoding = requests.get(OPEN_GEOCODING_URL, params_geocoding)
        res_geocoding.raise_for_status()
        data_geocoding = res_geocoding.json()
        geocoding_info = {
            'name': data_geocoding[0]['name'],
            'lat': data_geocoding[0]['lat'],
            'lon': data_geocoding[0]['lon']
        }
        params_weather = {"lat": geocoding_info["lat"], "lon": geocoding_info["lon"], "appid": API_KEY}
        res_weather = requests.get(OPEN_WEATHER_URL, params_weather)
        res_weather.raise_for_status()

        data_weather = res_weather.json()
        weather_info = {
            "city": data_weather["name"],
            "temperature": data_weather["main"]["temp"],
            "feels_like": data_weather["main"]["feels_like"],
            "humidity": data_weather["main"]["humidity"],
            "weather": data_weather["weather"][0]["main"],
            "wind_speed": data_weather["wind"]["speed"]
        }
        return weather_info
    except requests.exceptions.RequestException as ex:
        messagebox.showerror("Error", f"Failed to fetch currrent weather data: {ex}")
        return None

#Global setting don't touch
if __name__ == "__main__":
    init()