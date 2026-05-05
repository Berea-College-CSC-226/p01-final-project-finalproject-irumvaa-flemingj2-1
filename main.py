from classes.main_window import *
from classes.caesar_cipher import CaesarCipher
from classes.output_generator import OutputGenerator

def encode(_event, window, config):
    cipher = config["cipher"]
    update_key(_event, window, config)
    text = window.get_textbox_text("input")
    encoded = cipher.encode(text)
    window.set_textbox_text("output", encoded)
    window.fix_focus()
    return

def decode(_event, window, config):
    cipher = config["cipher"]
    update_key(_event, window, config)
    text = window.get_textbox_text("input")
    decoded = cipher.decode(text)
    window.set_textbox_text("output", decoded)

    window.fix_focus()
    return

def update_key(_event, window, config):
    cipher = config["cipher"]
    key_value = window.elements["entry"]["key"].get()

    if cipher.name.lower() == "caesar":
        try:
            cipher.key = int(key_value)
        except ValueError:
            cipher.key = 0
            window.alert("Please set key to number for CaserCipher!")
        except Exception as err:
            window.alert(err)

    window.fix_focus()
    return

def update_cipher(_event, window, ciphers, config):
    selection = window.get_combobox_text("cipher")
    use_cipher = ciphers[selection]
    config["cipher"] = use_cipher
    window.fix_focus()
    return

def update_output_type(_event, window, config):
    selection = window.get_combobox_text("output")
    config["output"] = selection
    window.fix_focus()
    return


def main():
    window = MainWindow()
    export = OutputGenerator()

    ciphers = {
        "caesar": CaesarCipher(0),
        "symbol": CaesarCipher(0)  # TODO
    }

    config = {
        "cipher": ciphers["caesar"],
        "output": "text"
    }

    window.create_gui()

    # ui elements to be used for bindings
    entry = window.elements["entry"]
    btn = window.elements["button"]
    combo = window.elements["combobox"]

    # bind events
    btn["encode"].bind("<Button-1>", lambda event: encode(event, window, config))
    btn["decode"].bind("<Button-1>", lambda event: decode(event, window, config))
    entry["key"].bind("<FocusOut>", lambda event: update_key(event, window, config))
    combo["cipher"].bind("<<ComboboxSelected>>", lambda event: update_cipher(event, window, ciphers, config))
    combo["output"].bind("<<ComboboxSelected>>", lambda event: update_output_type(event, window, config))

    window.root.mainloop()

if __name__ == "__main__":
    main()
