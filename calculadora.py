#! /usr/bin/python3.5

import sys

if len(sys.argv) != 4:
    sys.exit("Semántica: calc.py operacion operando1 operando2")

_, operation, firstArg, secondArg = sys.argv

try:

    firstArg = float(firstArg)
    secondArg = float(secondArg)
except ValueError:
    sys.exit("Semántica: calc.py operacion operando1 (int/float) operando2 (int/float)")

if operation == 'suma':
    result = firstArg + secondArg

elif operation == 'resta':
    result = firstArg - secondArg

elif operation == 'multiplicacion':
    result = firstArg * secondArg

elif operation == 'division':
    try:
        result = firstArg / secondArg
    except ZeroDivisionError:
        sys.exit('ERROR: división entre cero detectada')

else:
    sys.exit('Operación no comprendida. Prueba suma, resta, multiplicacion, division')

print(result)
