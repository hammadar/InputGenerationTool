import smtBoolean
import smtAssertion
import sys
import argparse

parser = argparse.ArgumentParser(description="Determine whether to output bools or bit vectors, and how many")
parser.add_argument("-n", metavar="nVariables", type=int, nargs=1, default=5)
parser.add_argument("-t", metavar="type", type=str, nargs=1, default="b", choices=["b", "v"])
args = parser.parse_args()

nVariables = args.n
typeInputs = args.t

names = []
start = "a"

for i in range(nVariables):
    names.append(chr(ord(start) + i))


booleans_vectors = []

for name in names:
    booleans_vectors.append(smtBoolean.smtBoolean(name))

assertion = smtAssertion.smtAssertion(booleans_vectors)




sys.stdout.write("(set-logic QF_BV)\n")

for boolean_vector in booleans_vectors:
    sys.stdout.write(boolean_vector.outputDeclaration())

sys.stdout.write(assertion.outputAssertion())