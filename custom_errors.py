"""
Custom errors classes
"""

class Error(Exception):
    """ Base class for exceptions """
    def __init__(self, message):
        super(Error, self).__init__(message)
        self.message = message

class ATMWithdrawalError(Error):
    """ Raised when a user inputs some amount that the ATM cannot service  """
