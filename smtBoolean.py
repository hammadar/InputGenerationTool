class smtBoolean:
    name: str

    def __init__(self, name):
        self.name = name

    def outputDeclaration(self):
        return ("(declare-fun " + self.name + "() Bool)\n")

    def outputName(self):
        return self.name