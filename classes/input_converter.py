######################################################################
# Author: Alain Irumva and Jayden Fleming
# Username: irumvaa and flemingj
#
# Assignment: P01
# Purpose: GUI Cipher Tool
######################################################################
# Acknowledgements:
# Original Homework 10 code was created by course staff.
####################################################################################
import os
from PIL import Image

class InputConverter:
    """
    Handles converting user input into a format
    usable by cipher classes.
    """
    def __int__(self, source=None):
        """Initializes the input source.
        Source can be a file path or raw text """
        self.source = source #stores the input source inside the object

    def detect_type(self, source):
        """detects the types of input source"""
        if isinstance(source, str):
            if os.path.isfile(source):
                return "file"
            return "text"
        return "unknown"

    def from_file(self, file_path):
        """
        Reads text input from a file and determines file type
        :param file_path:
        :return:
        """
        extension= os.path.splitext(file_path)[1].lower()
        if extension == ".txt":
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        elif extension in [".png", ".jpg", ".jpeg"]:
            return  self.from_image(file_path)
        else:
            raise ValueError("unsupported file type")

    def from_image(self, image_path):
        """
        Handles image input
        :param image_path:
        :return:
        """
        image = Image.open(image_path)
        return f"[IMAGE INPUT: {image.size}, mode={image.mode}]"

    def from_text(self, text):
        """
        Casts var to string
        :param text:
        :return:
        """
        if not isinstance((text, str)):
            raise ValueError("Input must be a string")
        return text

    def normalize(self, text):
        """

        :param text:
        :return:
        """
        return text.strip()

    def convert(self, source):
        """
        Gets text from given source
        :param source:
        :return:
        """
        input_type = self.detect_type(source)
        if input_type == "file":
            return self.normalize(self.from_file(source))
        elif input_type == "text":
            return self.normalize(self.from_text(source))
        else:
            raise ValueError("Unknown input type") #