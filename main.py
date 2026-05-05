from classes.main_window import *
from classes.caesar_cipher import CaesarCipher

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
    key_value = window.elements["entry"]["key"].get()

    if cipher.name.lower() == "caesar":
        try:
            cipher.key = int(key_value)
        except ValueError as err:
            cipher.key = 0
            window.alert("Please set key to number for CaserCipher!")
        except Exception as err:
            window.alert(err)

    return

def update_cipher(_event, window, ciphers):
    selection = window.elements["combobox"]["cipher"].get()
    use_cipher = ciphers["options"][selection]
    ciphers["selected"] = use_cipher
    return

def main():
    window = MainWindow()
    ciphers = {
        "selected": None,
        "options": {
            "caesar": CaesarCipher(0),
            "symbol": CaesarCipher(0) # TODO
        }
    }
    window.create_gui()

    # ui elements to be used for bindings
    entry = window.elements["entry"]
    btn = window.elements["button"]
    combo = window.elements["combobox"]

    # init default state selection
    update_cipher("init", window, ciphers)

    # bind events
    btn["encode"].bind("<Button-1>", lambda event: encode(event, window, ciphers["selected"]))
    btn["decode"].bind("<Button-1>", lambda event: decode(event, window, ciphers["selected"]))
    entry["key"].bind("<FocusOut>", lambda event: update_key(event, window, ciphers["selected"]))
    combo["cipher"].bind('<<ComboboxSelected>>', lambda event: update_cipher(event, window, ciphers))

    window.root.mainloop()

if __name__ == "__main__":
    main()
