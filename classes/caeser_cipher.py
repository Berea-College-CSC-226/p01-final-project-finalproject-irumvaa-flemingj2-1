#{from classes.base_cipher import BaseCipher
# class CaesarCipher(BaseCipher):
#     def ___init___(self, name, key):
#         super().___init___("Caesar", key)
#     def encode(self, text):
#         pass
#         #actual code
# #check the pics in my phone}
from classes.base_cipher import BaseCipher


class CaesarCipher(BaseCipher):
    """
    CaesarCipher implements a Caesar shift encryption by
    inheriting from the BaseCipher class.
    """

    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    def __init__(self, key):
        """
        Initializes the CaesarCipher with a shift key.
        """
        super().__init__("Caesar", key)

    def encode(self, text):
        """
        Encrypts text using a Caesar shift.
        """
        if not self.validate_input(text):
            raise ValueError("Invalid input text")

        result = ""

        for char in text.upper():
            if char in self.alphabet:
                index = self.alphabet.index(char)
                shifted_index = (index + self.key) % 26
                result += self.alphabet[shifted_index]
            else:
                result += char

        return result

    def decode(self, text):
        """
        Decrypts text by reversing the Caesar shift.
        """
        if not self.validate_input(text):
            raise ValueError("Invalid input text")

        result = ""

        for char in text.upper():
            if char in self.alphabet:
                index = self.alphabet.index(char)
                shifted_index = (index - self.key) % 26
                result += self.alphabet[shifted_index]
            else:
                result += char

        return result


