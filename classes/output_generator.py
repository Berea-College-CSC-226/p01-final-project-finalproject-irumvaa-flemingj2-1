######################################################################
# Author: Jayden Fleming, Alain Irumva
# Username: flemingj2, irumvaa
#
# Assignment: PO1
# Purpose: GUI Cipher Tool
######################################################################
# Acknowledgements: ./original_code/HW10
####################################################################################

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
        """
        return text

    def to_file(self, text, file_path):
        """
        Writes output text to a file.
        """
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(text)