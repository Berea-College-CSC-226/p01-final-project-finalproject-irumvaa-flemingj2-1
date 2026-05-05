from classes.main_window import *
from classes.caeser_cipher import CaesarCipher

def encode(_event, window, cipher):
    update_key(_event, window, cipher)
    text = window.get_textbox_text("input")
    encoded = cipher.encode(text)
    window.set_textbox_text("output", encoded)
    return

def decode(_event, window, cipher):
    update_key(_event, window, cipher)
    text = window.get_textbox_text("input")
    decoded = cipher.decode(text)
    window.set_textbox_text("output", decoded)
    return

def update_key(_event, window, cipher):
    window.root.focus()
    cipher.key = window.elements["entry"]["key"].get()
    return

def main():
    window = MainWindow()
    use_cipher = CaesarCipher(5)
    window.create_gui()

    entry = window.elements["entry"]
    btn = window.elements["button"]

    # bind events
    btn["encode"].bind("<Button-1>", lambda event: encode(event, window, use_cipher))
    btn["decode"].bind("<Button-1>", lambda event: decode(event, window, use_cipher))
    entry["key"].bind("<FocusOut>", lambda event: update_key(event, window, use_cipher))

    window.root.mainloop()

if __name__ == "__main__":
    main()
