import smtBoolean
import smtPair
import sys
import random

class smtAssertion:

    smtBooleans = []
    operations = ["and", "or", "=>"]
    smtPairs = []

    def __init__(self, smtBooleans):

        if smtBooleans is None:
            sys.stderr.write("Error in inputs\n")
            return

        self.smtBooleans = smtBooleans
        self.generatePairs()


    def generatePairs(self):
        numPairs = random.choice(range(1,3))
        lhs = None
        rhs = None
        operation = None

        for i in range(numPairs):
            x = random.choice([False, True])
            y = random.choice([False, True])
            if (not x):
                lhs = random.choice(self.smtBooleans)
            else:
                lhs = smtPair.smtPair(random.choice(self.smtBooleans), random.choice(self.smtBooleans), random.choice(self.operations))

            if (not y):
                rhs = random.choice(self.smtBooleans)
            else:
                rhs = smtPair.smtPair(random.choice(self.smtBooleans), random.choice(self.smtBooleans), random.choice(self.operations))

            operation = random.choice(self.operations)
            self.smtPairs.append(smtPair.smtPair(lhs, rhs, operation))


    def outputAssertion(self):
        assertion = "(assert "
        for pair in self.smtPairs:
            assertion += pair.outputPair()
        assertion += ")\n"

        return assertion




