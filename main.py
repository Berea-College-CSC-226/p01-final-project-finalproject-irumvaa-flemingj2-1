from classes.main_window import *
from classes.caeser_cipher import CaesarCipher

def encode(event, window, cipher):
    textbox = window.elements["textbox"]
    encoded = cipher.encode(textbox["input"].get(1.0, "end"))
    textbox["output"].delete(1.0, "end")
    textbox["output"].insert(1.0, encoded)
    return

def decode(event, window, cipher):
    textbox = window.elements["textbox"]
    encoded = cipher.decode(textbox["input"].get(1.0, "end"))
    textbox["output"].delete(1.0, "end")
    textbox["output"].insert(1.0, encoded)
    return

def main():
    window = MainWindow()
    use_cipher = CaesarCipher(5)
    window.create_gui()

    btn = window.elements["buttons"]

    # bind events
    btn["encode"].bind("<Button-1>", lambda event: encode(event, window, use_cipher))
    btn["decode"].bind("<Button-1>", lambda event: decode(event, window, use_cipher))

    window.root.mainloop()

if __name__ == "__main__":
    main()
