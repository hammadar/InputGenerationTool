import smtBoolean
import smtPair
import sys
import random

class smtAssertion:

    smtBooleans = []
    operations = ["and", "or", "=>"]
    smtPairs = smtPair.smtPair

    def __init__(self, smtBooleans):

        if smtBooleans is None:
            sys.stderr.write("Error in inputs\n")
            return

        self.smtBooleans = smtBooleans
        self.generatePairs()


    def generatePairs(self):
        numPairs = random.choice(range(1,10))
        '''lhs = None
        rhs = None
        operation = None

        for i in range(numPairs):
            x = random.choice([False, True])
            if (i == (numPairs - 1)):
                y = random.choice([False, True])
            else:
                y = True
            if (not x):
                lhs = random.choice(self.smtBooleans)
            else:
                lhs = smtPair.smtPair(random.choice(self.smtBooleans), random.choice(self.smtBooleans), random.choice(self.operations))

            if (not y):
                rhs = random.choice(self.smtBooleans)
            else:
                rhs = smtPair.smtPair(random.choice(self.smtBooleans), random.choice(self.smtBooleans), random.choice(self.operations))

            operation = random.choice(self.operations)
            self.smtPairs.append(smtPair.smtPair(lhs, rhs, operation))'''
        self.smtPairs = self.generateNewPairs(0, numPairs)


    def outputAssertion(self):
        assertion = "(assert "
        assertion += self.smtPairs.outputPair()
        assertion += ")\n"

        return assertion

    def generateNewPairs(self,i, numPairs):
        left = random.choice([False, True])
        pair = smtPair.smtPair()
        innerPair = smtPair.smtPair()

        if (left):
            innerPair.setLHS(random.choice(self.smtBooleans))
            innerPair.setRHS(random.choice(self.smtBooleans))
            innerPair.setOperation(random.choice(self.operations))
            pair.setLHS(innerPair)
            pair.setOperation(random.choice(self.operations))
            if i == (numPairs-1):
                pair.setRHS(random.choice(self.smtBooleans))
            else:
                pair.setRHS(self.generateNewPairs(i+1, numPairs))
            return pair
        else:
            pair.setLHS(random.choice(self.smtBooleans))
            pair.setOperation(random.choice(self.operations))
            pair.setRHS(random.choice(self.smtBooleans))
            if i == (numPairs-1):
                pair.setRHS(random.choice(self.smtBooleans))
            else:
                pair.setRHS(self.generateNewPairs(i+1, numPairs))
            return pair





