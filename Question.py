# This file sets initializes an instance of the Question class and sets its description and list of answers.
class Question:
    """Question class"""

    def __init__(self, description):
        """Initializes a question

        Args:

            description(string): description of question

         """
        self._description = description
        self._answers = []  # an empty list of answers for each question

    @property
    def answers(self):
        """Returns list of answers for each question."""
        return self._answers

    @answers.setter
    def answers(self, value):
        """Sets the list of answers for each question."""
        self._answers = value

    @property
    def description(self):
        """"Returns the description for each question."""
        return self._description

    @description.setter
    def description(self, value):
        """"Sets the description for each question."""
        self._description = value
