class MorseCodeConverter:
    """
    Class to handle the conversion of text to Morse code.

    Attributes:
    - morse_code_dict: dict
        A dictionary containing the mapping of characters to their respective Morse code representation.
    """

    def __init__(self):
        """
        Constructor to instantiate the MorseCodeConverter class.

        Initializes the morse_code_dict attribute with the mapping of characters to Morse code.
        """

        self.morse_code_dict = {
            'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
            'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
            'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
            'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
            '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-', ',': '--..--',
            '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
            ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
            '$': '...-..-', '@': '.--.-.', ' ': '/'
        }

    def convert_to_morse_code(self, text: str):
        """
        Converts the given text to Morse code.

        Parameters:
        - text: str
            The text to be converted to Morse code.

        Returns:
        - str:
            The Morse code representation of the input text.
        """

        # Converting the text to uppercase for consistency
        text = text.upper()

        # Initializing an empty string to store the Morse code representation
        morse_code = ""

        # Iterating through each character in the text
        for char in text:
            # Checking if the character is present in the Morse code dictionary
            if char in self.morse_code_dict:
                # Appending the Morse code representation of the character to the result string
                morse_code += self.morse_code_dict[char] + " "

        # Returning the Morse code representation
        return morse_code.strip()


# Example usage of the MorseCodeConverter class:

# Creating an instance of the MorseCodeConverter class
converter = MorseCodeConverter()

# Converting a text to Morse code
text = "Hello, World!"
morse_code = converter.convert_to_morse_code(text)
print(f"The Morse code representation of '{text}' is: {morse_code}")
