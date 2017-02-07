#! /usr/bin/python3.5
import sys

arguments = sys.argv

operation = arguments[1]
firstArg = int(arguments[2])
secondArg = int(arguments[3])


if operation == 'suma':
	charOp = '+'
	result = firstArg + secondArg

elif operation == 'resta':
	charOp = '-'
	result = firstArg - secondArg

elif operation == 'multiplicacion':
	charOp = '*'
	result = firstArg * secondArg

elif operation == 'division':
	charOp = '/'
	try:
		result = firstArg / secondArg
	except ZeroDivisionError:
		sys.exit("Error: división entre cero no permitida")

else:
	sys.exit("Operación no reconocida. suma, resta, multiplicacion, division")

print(firstArg, charOp, secondArg, '=', result)
