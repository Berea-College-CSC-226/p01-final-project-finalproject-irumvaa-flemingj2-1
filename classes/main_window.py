import tkinter as tk
from tkinter import ttk


class MainWindow:
    def __init__(self):
        self.elements = {
            "frames": {},
            "buttons": {}
        }
        self.root = tk.Tk()
        self.root.minsize(width=350, height=300)
        self.root.maxsize(width=350, height=300)
        self.root.title("Cipher Tool")

    def create_gui(self):
        elm = self.elements
        btn = elm["buttons"]
        frame = elm["frames"]
        wpx, hpx = self.wpx, self.hpx

        frame["top_left"] = ttk.Frame(self.root, width=wpx(0.2), height=hpx(0.2))
        btn["encode"] = tk.Button(frame["top_left"], text="Encode")
        btn["decode"] = tk.Button(frame["top_left"], text='Decode')


        frame["top_left"].grid(row=0, column=0)

        for k, v in btn.items():
            v.pack(expand=True)


    def hpx(self, percent):
        return self.sz(percent, axis="h")

    def wpx(self, percent):
        return self.sz(percent, "w")

    def sz(self, percent, axis):
        """
        Takes percent (0-1) of given window axis "w" or "h" and returns as pixels.
        :param axis: Window axis
        :param percent: Percent of window
        :return: Pixels
        """
        w,h = self.root.winfo_width(), self.root.winfo_height()
        if axis == "w":
            return w * percent
        elif axis == "h":
            return h * percent
        else:
            return 0


