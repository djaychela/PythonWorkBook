import tkinter as tk
import screeninfo

root = tk.Tk()

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

print(f"Width: {screen_width} Height: {screen_height}")

for m in screeninfo.get_monitors('osx'):
    print(m)