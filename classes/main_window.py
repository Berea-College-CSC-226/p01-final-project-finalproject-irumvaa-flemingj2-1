import tkinter as tk

from rdkit.Dbase.DbModule import placeHolder


class MainWindow:
    def __init__(self):
        self.elements = {
            "frames": {},
            "buttons": {},
            "textbox": {}
        }
        self.root = tk.Tk()
        self.root.minsize(width=450, height=300)
        self.root.maxsize(width=450, height=300)
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
        frame["left_nav"] = tk.Frame(self.root, width=wpx(0.2), height=hpx(1), bg="#f1f0ea")
        frame["right"] = tk.Frame(self.root, bg="#f1f0ea")
        
        # init buttons
        btn["encode"] = tk.Button(frame["left_nav"], text="Encode")
        btn["decode"] = tk.Button(frame["left_nav"], text='Decode')

        # init textboxes
        textbox["input"] = tk.Text(frame["right"], height=1)
        textbox["output"] = tk.Text(frame["right"], height=1)
        textbox["input"].insert(1.0, "input(placeholder)")
        textbox["output"].insert(1.0, "output(placeholder)")

        # configure layout
        frame["left_nav"].pack(side=tk.LEFT, fill=tk.Y)
        frame["right"].pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        btn["encode"].pack(side=tk.TOP, padx=20, pady=5)
        btn["decode"].pack(side=tk.TOP, padx=20, pady=5)
        textbox["input"].pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=10)
        textbox["output"].pack(side=tk.BOTTOM, fill=tk.BOTH ,expand=True, pady=10)

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