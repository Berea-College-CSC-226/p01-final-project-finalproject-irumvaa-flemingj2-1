import tkinter as tk

my_theme = {
    "base": "#474448",
    "crust": "#ffffff",
    "bg1": "#454545",
    "fg1": "#ccdfdf",
}

class MainWindow:
    def __init__(self):
        self.elements = {
            "frames": {},
            "buttons": {},
            "textbox": {}
        }
        self.theme = my_theme
        self.root = tk.Tk()
        self.root.minsize(width=470, height=300)
        self.root.maxsize(width=470, height=300)
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
        theme = self.theme
        wpx, hpx = self.wpx, self.hpx

        # init frames
        frame["left_nav"] = tk.Frame(self.root, width=wpx(0.2), height=hpx(1), bg=theme["crust"])
        frame["right"] = tk.Frame(self.root, bg=theme["base"])
        frame["input"] = tk.LabelFrame(frame["right"], text="Input", bg=theme["crust"])
        frame["output"] = tk.LabelFrame(frame["right"], text="Output", bg=theme["crust"])
        
        # init buttons
        btn["encode"] = tk.Button(frame["left_nav"], text="Encode", bg=theme["bg1"], fg=theme["fg1"])
        btn["decode"] = tk.Button(frame["left_nav"], text="Decode", bg=theme["bg1"], fg=theme["fg1"])

        # init textboxes
        textbox["input"] = tk.Text(frame["input"], height=1)
        textbox["output"] = tk.Text(frame["output"], height=1)


        # configure layout
        frame["left_nav"].pack(side=tk.LEFT, fill=tk.Y, expand=True)
        frame["right"].pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        frame["input"].pack(side=tk.TOP, fill=tk.BOTH, expand=True, pady=10)
        frame["output"].pack(side=tk.BOTTOM, fill=tk.BOTH, expand=True, pady=10)
        btn["encode"].pack(side=tk.TOP, padx=20, pady=5)
        btn["decode"].pack(side=tk.TOP, padx=20, pady=5)
        textbox["input"].pack(fill=tk.BOTH, expand=True)
        textbox["output"].pack(fill=tk.BOTH, expand=True)

    def get_textbox_text(self, box):
        textbox = self.elements["textbox"][box]
        return textbox.get(1.0, "end")

    def set_textbox_text(self, box, text):
        textbox = self.elements["textbox"][box]
        textbox.delete(1.0, "end")
        textbox.insert(1.0, text)
        return

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