import tkinter as tk
window = tk.Tk()

width = 600
height = 400
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
center_x = int(screen_width/2 - width/2)
center_y = int(screen_height/2 - height/2)


window.title('Clock')
window.geometry(f'{width}x{height}+{center_x}+{center_y}')

label = tk.Label(window, text='abc', font=('Helvectia', 24))
label = tk.Label(window, text='def', font=('Helvectia', 24))

label.pack(ipady=100)

window.mainloop()