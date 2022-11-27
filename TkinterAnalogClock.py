import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.wm_title("Tkinter clock")
root.geometry("1000x1000")

class App:
    def __init__(self, root):
        self.root = root

    def create_clock(self):
        pass

    def clock(self):
        pass


def create_circle(x, y, r, canvas, fill='white', width=1):
    x0 = x-r
    x1 = x+r
    y0 = y-r
    y1 = y+r
    canvas.create_oval(x0, y0, x1, y1, fill=fill, width=width)


canvas = tk.Canvas(width=1000, height=1000, bg="white")
canvas.pack()
create_circle(500, 500, 200, canvas, 'grey', 5)
create_circle(500, 500, 3, canvas, 'black')
root.mainloop()
