import tkinter
import tkinter as tk
from tkinter import ttk


class MainWindow:
    def __init__(self):
        self.elements = {
            "frames": {},
            "buttons": {},
            "textbox": {}
        }
        self.root = tk.Tk()
        self.root.minsize(width=350, height=300)
        self.root.maxsize(width=3501, height=3001)
        self.root.title("Cipher Tool")
        self.root.config(bg="#474448")
        self.root.update_idletasks()

    def create_gui(self):
        """
        Creates & setup elements for window
        :return:
        """
        elm = self.elements
        btn = elm["buttons"]
        frame = elm["frames"]
        textbox = elm["textbox"]
        wpx, hpx = self.wpx, self.hpx

        # init frames
        frame["top_left"] = tk.Frame(self.root, width=wpx(0.2), height=hpx(0.2), bg="#f1f0ea")

        # init buttons
        btn["encode"] = tk.Button(frame["top_left"], text="Encode")
        btn["decode"] = tk.Button(frame["top_left"], text='Decode')

        # init textboxes
        textbox["encode"] = tk.Text(frame["top_left"])
        textbox["decode"] = tk.Text(frame["top_left"])

        # configure layout
        frame["top_left"].pack(side=tk.LEFT, fill=tk.Y)
        btn["encode"].pack(side=tk.TOP, padx=20, pady=5)
        btn["decode"].pack(side=tk.TOP, padx=20, pady=5)

    def hpx(self, percent):
        """
        Percent height to pixels
        :param percent:
        :return: pixels
        """
        return self.sz(percent, axis="h")

    def wpx(self, percent):
        """
        Percent width to pixels
        :param percent:
        :return: pixels
        """
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
            return (w * percent) // 1
        elif axis == "h":
            return (h * percent) // 1
        else:
            return 0