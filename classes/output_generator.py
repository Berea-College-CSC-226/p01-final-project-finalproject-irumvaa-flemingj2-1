
######################################################################
# Author: Alain Irumva and Jayden Fleming
#
# Assignment: Final Project - Cipher Tool
#
# Purpose:
# This class handles all output operations for the program.
# It is responsible for formatting the output and saving
# results to a file when needed.
######################################################################

class OutputGenerator:
    """
    Handles formatting and exporting cipher output.
    """

    def __init__(self):
        """
        Initializes the output generator.
        """
        pass

    def to_text(self, text):
        """
        Returns formatted output for display.
        :param text: processed cipher text
        :return: formatted text for display

        """
        return text

    def to_file(self, text, file_path):
        """
        Writes output text to a file.
        :param text: processed cipher text
        :param file_path: path where the file will be saved
        :return: None

        """
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)