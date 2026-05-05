
######################################################################
# Author: Alain Irumva and Jayden Fleming
#
# Assignment: Final Project - Cipher Tool
#
# Purpose:
# This class handles all input processing for the program. It detects
# whether the input is text or a file, reads the input, and prepares
# it for use by cipher classes.
######################################################################

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
        """detects the types of input source
        :param source: input value (text or file path)
        :return: "file", "text", or "unknown" """

        if isinstance(source, str):
            if os.path.isfile(source):
                return "file"
            return "text"
        return "unknown"

    def from_file(self, file_path):
        """
        Reads text input from a file and determines file type
        :param file_path: path to file
        :return: file content (text or image metadata
        """
        extension= os.path.splitext(file_path)[1].lower() #get file extension
        if extension == ".txt": #handles text files
            with open(file_path, "r", encoding="utf-8") as file:
                return file.read()
        elif extension in [".png", ".jpg", ".jpeg"]:
            return  self.from_image(file_path)
        else:
            raise ValueError("unsupported file type")

    def from_image(self, image_path):
        """
        Handles image input
        :param image_path: path to image file
        :return: string describing image size and mode
        """
        image = Image.open(image_path)
        return f"[IMAGE INPUT: {image.size}, mode={image.mode}]"

    def from_text(self, text):
        """
        Accepts direct text input (GUI or CLI)
        :param text: raw input text
        :return: validated tex
        """
        if not isinstance((text, str)):
            raise ValueError("Input must be a string")
        return text

    def normalize(self, text):
        """
        Normalizes text for cipher processing
        :param text: input text
        :return: cleaned text
        """
        return text.strip()

    def convert (self, source):
        """Detects input type and routes it to the correct handler.
    :param source: input text or file path
    :return: processed string ready for cipher"""
        input_type = self.detect_type(source) #Handles file input
        if input_type == "file":
            return self.normalize(self.from_file(source))
        elif input_type == "text":
            return self.normalize(self.from_text(source))
        else:
            raise ValueError("Unknown input type")