# This file initializes an instance of the Answer class and sets description for the answer
# and checks if the user's answer is correct.
class Answer:
    """Answer class"""

    def __init__(self, description, is_correct):
        """Initializes a question

        Args:

            description(string): description of each answer
            is_correct(bool): if the answer is correct, it evaluates to true, else it evaluates to false


         """
        self._description = description
        self._is_correct = is_correct

    @property
    def description(self):
        """Returns a description of the answer."""
        return self._description

    @description.setter
    def description(self, value):
        """Sets a description of the answer.If the passed argument is "", then the program raises Type Error."""
        if value == "":
            raise TypeError("Invalid format.")
        else:
            self._description = value

    @property
    def is_correct(self):
        """Returns True or False if the answer is correct."""
        return self._is_correct

    @is_correct.setter
    def is_correct(self, value):
        """Sets True or False if the answer is correct.If the passed argument is "", then the program raises Type
        Error. """
        self._is_correct = value
