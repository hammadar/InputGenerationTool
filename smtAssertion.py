import smtBoolean
import sys
import random

class smtAssertion:

    smtBooleans = []
    operations = ["and", "or", "not", "=>", "<=>"]

    def __init__(self, smtBooleans, assertions):

        if smtBooleans is None or assertions is None:
            sys.stderr.write("Error in inputs\n")
            return

        self.smtBooleans = smtBooleans

