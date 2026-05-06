######################################################################
# Author: Jayden Fleming, Alain Irumva
# Username: flemingj2, irumvaa
#
# Assignment: PO1
# Purpose: GUI Cipher Tool
######################################################################
# Acknowledgements:
# - https://www.momjunction.com/articles/secret-ciphers-codes-for-kids_00736353/
####################################################################################
from classes.base_cipher import BaseCipher

class MorseCipher(BaseCipher):
    """
    MorseCipher is a morse-code translator.
    """
    separator_char = "|"
    def __init__(self):
        """
        Init cipher.
        """
        super().__init__("Morse", 0)
        self.morse_map = (
            ("a", ".-"),
            ("b", "-..."),
            ("c", "-.-."),
            ("d", "-.."),
            ("e", "."),
            ("f", "..-."),
            ("g", "--."),
            ("h", "...."),
            ("i", ".."),
            ("j", ".---"),
            ("k", "-.-"),
            ("l", ".-.."),
            ("m", "--"),
            ("n", "-."),
            ("o", "---"),
            ("p", ".--."),
            ("q", "--.-"),
            ("r", ".-."),
            ("s", "..."),
            ("t", "-"),
            ("u", "..-"),
            ("v", "...-"),
            ("w", ".--"),
            ("x", "-..-"),
            ("y", "-.--"),
            ("z", "--.."),
            ("1", ".----"),
            ("2", "..---"),
            ("3", "...--"),
            ("4", "....-"),
            ("5", "....."),
            ("6", "-...."),
            ("7", "--..."),
            ("8", "---.."),
            ("9", "----."),
            ("0", "-----"),
            (" ", " ")
        )

    def encode(self, text):
        """
        Encrypts text using morse_map.
        """
        result = ""

        if not self.validate_input(text):
            raise ValueError("Invalid input text")

        for char in text:
            if char == self.separator_char:
                return ValueError("Invalid input. '{0}' is a reserved character".format(self.separator_char))

        for char in text:
            found_pair = False

            for pair in self.morse_map:
                if char.lower() == pair[0]:
                    found_pair = True
                    result += pair[1]
                    result += "|"
                    break

            if not found_pair:
                result += char

        return result

    def decode(self, text):
        """
        Decodes text using morse_map.
        :param text:
        :return:
        """
        result = ""

        if not self.validate_input(text):
            raise ValueError("Invalid input text")

        for char_set in text.split(self.separator_char):
            found_pair = False

            for pair in self.morse_map:
                if char_set == pair[1]:
                    found_pair = True
                    result += pair[0]
                    break

            if not found_pair:
                result += char_set

        return result