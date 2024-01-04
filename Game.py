
# This file initializes an instance of the Game class and sets the list of questions for the game.

class Game:
    """Game class"""

    def __init__(self, user):
        """Initializes a game

        Args:

            user(User): an instance of the User class


         """
        self._user = user
        self._questions = []

    @property
    def questions(self):
        """Returns the list of questions."""
        return self._questions

    @questions.setter
    def questions(self, value):
        """"Sets the list of questions if the passed argument is not equal to ""(raises TypeError)."""
        if value == "":
            raise TypeError("Incorrect format.")
        else:
            self._questions = value
# @property
# def user(self):
#  """Returns an instance of the User class."""
#   return self._user

# @user.setter
# def user(self, value):
#  """Sets an instance of the User class."""
#   self._user = value

# @property
# def questions(self):
#  """Returns the list of questions."""
#   return self._questions

# @questions.setter
# def questions(self, value):
#    """Sets the list of questions."""
#    self._questions = value

#    def get_result(self):
#        return self._questions.
