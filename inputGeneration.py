import smtBoolean
import smtAssertion

names = ["a", "b", "c", "d", "e", "f", "g", "h"]
booleans = []

for name in names:
    booleans.append(smtBoolean.smtBoolean(name))

assertion = smtAssertion.smtAssertion(booleans)
print(assertion.outputAssertion())