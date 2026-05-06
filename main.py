######################################################################
# Author: Jayden Fleming, Alain Irumva
# Username: flemingj2, irumvaa
#
# Assignment: PO1
# Purpose: GUI Cipher Tool
####################################################################################
from classes.main_window import MainWindow
from classes.output_generator import OutputGenerator
from classes.caesar_cipher import CaesarCipher
from classes.morse_cipher import MorseCipher

def encode(_event, window, config, exporter):
    """
    Encode connective logic
    :param _event:
    :param window:
    :param config:
    :param exporter:
    :return:
    """
    cipher = config["cipher"]
    update_key(_event, window, config)
    text = window.get_textbox_text("input")
    encoded = cipher.encode(text)

    if config["output"] == "text":
        window.set_textbox_text("output", encoded)
    elif config["output"] == "file":
        exporter.to_file(encoded, "out_encoded.txt")
        window.alert("Encoded text written to: ./out_encoded.txt")

    window.fix_focus()
    return

def decode(_event, window, config, exporter):
    """
    Decode connective logic
    :param _event:
    :param window:
    :param config:
    :param exporter:
    :return:
    """
    cipher = config["cipher"]
    update_key(_event, window, config)
    text = window.get_textbox_text("input")
    decoded = cipher.decode(text)

    if config["output"] == "text":
        window.set_textbox_text("output", decoded)
    elif config["output"] == "file":
        exporter.to_file(decoded, "out_decoded.txt")
        window.alert("Decoded text written to: ./out_decoded.txt")

    window.fix_focus()
    return

def update_key(_event, window, config):
    """
    Update cipher key
    :param _event:
    :param window:
    :param config:
    :return:
    """
    cipher = config["cipher"]
    key_value = window.elements["entry"]["key"].get()

    if cipher.name.lower() == "caesar":
        try:
            cipher.key = int(key_value)
        except ValueError:
            cipher.key = 0
            window.alert("Please set key to number for CaesarCipher!")
        except Exception as err:
            window.alert(err)

    window.fix_focus()
    return

def update_cipher(_event, window, ciphers, config):
    """
    Update config cipher
    :param _event:
    :param window:
    :param ciphers:
    :param config:
    :return:
    """
    selection = window.get_combobox_text("cipher")
    use_cipher = ciphers[selection]
    config["cipher"] = use_cipher
    window.fix_focus()
    return

def update_output_type(_event, window, config):
    """
    Update config output type
    :param _event:
    :param window:
    :param config:
    :return:
    """
    selection = window.get_combobox_text("output")
    config["output"] = selection
    window.fix_focus()
    return


def main():
    """
    Core logic
    :return:
    """
    # init classes
    window = MainWindow()
    exporter = OutputGenerator()

    # mutating vars
    ciphers = {
        "caesar": CaesarCipher(0),
        "symbol": None,  # TODO
        "morse": MorseCipher()
    }

    config = {
        "cipher": ciphers["caesar"],
        "output": "text"
    }

    # init ui elements
    window.create_gui()

    # ui elements to be used for bindings
    entry = window.elements["entry"]
    btn = window.elements["button"]
    combo = window.elements["combobox"]

    # bind events
    btn["encode"].bind("<Button-1>", lambda event: encode(event, window, config, exporter))
    btn["decode"].bind("<Button-1>", lambda event: decode(event, window, config, exporter))
    entry["key"].bind("<FocusOut>", lambda event: update_key(event, window, config))
    combo["cipher"].bind("<<ComboboxSelected>>", lambda event: update_cipher(event, window, ciphers, config))
    combo["output"].bind("<<ComboboxSelected>>", lambda event: update_output_type(event, window, config))

    # start event loop
    window.root.mainloop()

if __name__ == "__main__":
    main()
