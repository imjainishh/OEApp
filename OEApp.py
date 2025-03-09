#import library
import tkinter as tk

def init():
    #Init window
    root = tk.Tk()
    root.geometry('540x350')
    root.maxsize(540,340)
    root.title("Ontario Emergency App")
    #Init Frames
    frame_main = tk.Frame()
    frame_911 =  tk.Frame()
    #Init Menu bar widget
    menu_bar = tk.Menu(frame_main)
    #Cascade menu
    emergency_menu = tk.Menu(menu_bar, tearoff=0)
    menu_bar.add_cascade(label = "Emergency Contact", menu = emergency_menu)
    emergency_menu.add_command(label = "Call 911", command = None)
    emergency_menu.add_command(label = "Call fire departement",  command =  None)
    emergency_menu.add_command(label = "Call 511",  command =  None)
    #Standalone menu
    menu_bar.add_command(label = "Wild fire alerts", command = None)
    menu_bar.add_command(label = "Weather updates", command = None)
    menu_bar.add_command(label = "Interactive map", command = None)
    menu_bar.add_command(label = "Evacuation estimation", command = None)
    menu_bar.add_command(label = "About", command = None)
    #Display Widget
    root.config(menu=menu_bar)
    root.mainloop()



#Global setting don't touch
if __name__ == "__main__":
    init()