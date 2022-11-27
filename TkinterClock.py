import tkinter as tk
from datetime import datetime


class App:
    def __init__(self, root):
        self.root = root
        self.text = tk.StringVar()
        self.ampm_text = tk.StringVar()
        self.date_text = tk.StringVar()
        self.time_label = tk.Label(root, textvariable=self.text, font=('Helvectia', 48))
        self.time_label.place(x=300, y=10)
        self.ampm_label = tk.Label(root, textvariable=self.ampm_text, font=('Helvectia', 24), foreground='grey')
        self.ampm_label.place(x=560, y=39)
        self.date_label = tk.Label(root, textvariable=self.date_text, font=('Helvectia', 18), foreground='blue')
        self.date_label.place(x=300, y=80)

    def show_time(self):
        time = datetime.now()
        self.text.set(time.strftime('%I:%M:%S'))
        self.ampm_text.set(time.strftime('%p'))
        self.date_text.set(time.strftime('%A, %B %d, %Y'))

    def clock(self):
        self.root.after(40, self.clock)
        self.show_time()


root = tk.Tk()
app = App(root)
root.wm_title("Tkinter clock")
root.geometry("1000x1000")
root.after(0, app.clock)
root.mainloop()
