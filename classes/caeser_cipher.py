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

        for char in text:
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


