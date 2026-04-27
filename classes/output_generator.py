
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