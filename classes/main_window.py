######################################################################
# Author: Alain Irumva and Jayden Fleming
# Username: irumvaa and jfleming
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