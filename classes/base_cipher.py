######################################################################
# Author: Alain Irumva and Jayden Fleming
# Username: irumvaa and flemingj
#
# Assignment: Final project (HW10 Expansion): Base Cipher System
#
# Purpose: Define a base cipher class to support multiple encryption
#          and decryption algorithms (e.g., Caesar, GY) with a shared
#          interface for encoding, decoding, and validation.
#
######################################################################
# Acknowledgements:
# Original Homework 10 code was created by course staff.
####################################################################################

class BaseCipher:
    """
    Base class for all ciphers.
    """

    def __init__(self, name, key):
        """
        Initializes the cipher name and key.

        :param name: Name of the cipher (e.g., "Caesar", "GY")
        :param key: Key used for encoding/decoding
        """
        self.name = name
        self.key = key

    def encode(self, text):
        """
        Encrypts the given input text using the cipher's rules.

        :param text: plaintext input
        :return: encrypted text
        """
        raise NotImplementedError("encode() must be implemented by subclass") #Forces child classes to implement their own encode logic

    def decode(self, text):
        """
        Decrypts the given input text using the cipher's rules.
        This method should be overridden by subclasses.

        :param text: encrypted input
        :return: decrypted text
        """
        raise NotImplementedError("decode() must be implemented by subclass")

    def validate_input(self, text):
        """
        Checks if the input text is valid for the cipher.
        Default behavior ensures the input is a string.

        :param text: input text
        :return: True if valid, False otherwise
        """
        return isinstance(text, str)
