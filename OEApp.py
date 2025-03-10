#import library
import tkinter as tk
import webbrowser

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


def set_511_frame(frame):
    #Call 511 frames
    pass

def set_fd_frame(frame):
    #Call fire dept frames
    pass

def set_weather_frame(frame):
    #Get weather update
    pass

def set_wildfire_frame(frame):
    #Get wildfire alert
    pass

def set_map_frame(frame):
    #Show wild fire interactive map
    pass

def set_evacuation_frame(frame):
    #Evacuation estimate calculator
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

#Global setting don't touch
if __name__ == "__main__":
    init()