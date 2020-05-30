import smtBoolean
import smtAssertion
import sys

names = ["a", "b", "c", "d", "e", "f", "g", "h"]
booleans = []

for name in names:
    booleans.append(smtBoolean.smtBoolean(name))

assertion = smtAssertion.smtAssertion(booleans)

for boolean in booleans:
    sys.stdout.write(boolean.outputDeclaration())

sys.stdout.write(assertion.outputAssertion())