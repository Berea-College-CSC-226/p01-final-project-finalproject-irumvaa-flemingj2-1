import tkinter as tk

class MainWindow:
    def __init__(self):
        self.elements = None
        self.root = tk.Tk()

        self.root.minsize(width=350, height=300)
        self.root.maxsize(width=350, height=300)
        self.root.title("Cipher Tool")
        #self.root.grid_slaves()

    def create_gui(self):
        self.elements = {
            "btn_encode": tk.Button(self.root, text="Encode"),
            "btn_decode": tk.Button(self.root, text="Decode")
        }

        self.elements.get("btn_encode").grid(row=0, column=0)
        self.elements.get("btn_decode").grid(row=1, column=0)
