
class InputConverter:
    """
    Handles converting user input into a format
    usable by cipher classes.
    """
    def __int__(self, source=None):
        """Initializes the input source.
        Source can be a file path or raw text """
        self.source = source #stores the input source inside the object

    def from_file(self, file_path):
        """ Reads text input from a file"""
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()

    def from_text(self, text):
        """ Accepts direct text input (GUI or CLI)"""
        if not isinstance((text, str)):
            raise ValueError("Input must be a string")
        return text

    def normalize(self, text):
        """ Normalizes text for cipher processing"""
        return text.strip()