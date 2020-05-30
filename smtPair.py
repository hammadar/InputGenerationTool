import smtBoolean

class smtPair:
    lhs = None
    rhs = None
    operation = None

    def __init__(self, lhs, rhs, operation):
        self.lhs = lhs
        self.rhs = rhs
        self.operation = operation

    def outputPair(self):
        expressionToReturn = "(" + self.operation + " "

        if (isinstance(self.lhs, smtPair)):
            expressionToReturn += self.lhs.outputPair()
        else:
            expressionToReturn += self.lhs.outputName()

        expressionToReturn += " "

        if (isinstance(self.rhs, smtPair)):
            expressionToReturn += self.rhs.outputPair()
        else:
            expressionToReturn += self.rhs.outputName()

        expressionToReturn += ")"
        return expressionToReturn