
######################################################################
# Author: Alain Irumva and Jayden Fleming
#
# Assignment: Final Project - Cipher Tool
#
# Purpose:
# This class implements a Caesar cipher by extending BaseCipher.
# It encrypts and decrypts text using a shift key while preserving
# letter case and leaving non-alphabet characters unchanged.
######################################################################
from classes.base_cipher import BaseCipher

class CaesarCipher(BaseCipher):
    """
    CaesarCipher implements a Caesar shift encryption by
    inheriting from the BaseCipher class.
    """

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ" # Alphabet used for shifting letters

    def __init__(self, key):
        """
        Initializes the CaesarCipher with a shift key.
        Param key: integer value used for shifting characters
        """
        super().__init__("Caesar", key)

    def encode(self, text):
        """
        Encrypts text using a Caesar shift.

        Each letter is shifted forward by the key value.
        Uppercase and lowercase letters are preserved.
        Non-letter characters are unchanged.

        :param text: plaintext input string
        :return: encrypted text string
        """
        if not self.validate_input(text): #Validate input
            raise ValueError("Invalid input text")

        result = ""

        for char in text:
            #Assume lowercase unless found in uppercase alphabet
            is_lower = True
            if char in self.alphabet.upper():
                is_lower = False

            if char.lower() in self.alphabet.lower():
                index = self.alphabet.lower().index(char.lower())
                shifted_index = (index + self.key) % len(self.alphabet)
                if is_lower:
                    result += self.alphabet[shifted_index].lower()
                else:
                    result += self.alphabet[shifted_index].upper()
            else: #keep non-letter characters unchanged
                result += char

        return result

    def decode(self, text):
        """
        Decrypts text by reversing the Caesar shift.

        Each letter is shifted backward by the key value.
        Uppercase and lowercase letters are preserved.
        Non-letter characters remain unchanged.

        :param text: encrypted text string
        :return: original decrypted text
        """
        if not self.validate_input(text):
            raise ValueError("Invalid input text")

        result = ""

        for char in text:
            is_lower = True
            if char in self.alphabet.upper():
                is_lower = False

            if char.lower() in self.alphabet.lower():
                index = self.alphabet.lower().index(char.lower())
                shifted_index = (index - self.key) % len(self.alphabet)
                if is_lower:
                    result += self.alphabet[shifted_index].lower()
                else:
                    result += self.alphabet[shifted_index].upper()

            else:
                result += char

        return result


