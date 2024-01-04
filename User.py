import re


# This file initializes an instance of the User class and sets its username.

class User:
    """User class"""

    def __init__(self):
        """Initializes a user


         """
        self._name = None

    @property
    def name(self):
        """Returns the name of the user."""
        return self._name

    @name.setter
    def name(self, value):
        """Sets the name of the user."""
        self._name = value
