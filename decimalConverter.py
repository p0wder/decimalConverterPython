"""
Author: Scott C Gramig
Program: Decimal to Binary, Hexadecimal, and Octal converter
"""

# Decimal to Binary
def binary(decInput):
	result = []

	while decInput != 0:
		if (decInput % 2) == 0:
			result.append('0')
		else:
			result.append('1')

		decInput /=2

	result.reverse()

	return result


# Decimal to Hexadecimal
def hexi(decInput):
	result = []
	output = []

	#dict for converting values to hex
	conversionDict = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8',
			9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F' }

	while decInput != 0:
		result.append(decInput % 16)
		decInput /= 16

	result.reverse()

	for x in result:
		output.append(conversionDict.get(x))

	return output


# Decimal to Octal
def octal(decInput):
	result = []
	output = []

	#dict for converting values to octal
	conversionDict = { 0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '10',
			9: '11', 10: '12', 11: '13', 12: '14', 13: '15', 14: '16', 15: '17', 16: '20' }

	while decInput != 0:
		result.append(decInput % 8)
		decInput /= 8

	result.reverse()

	for x in result:
		output.append(conversionDict.get(x))

	return output


print "-------- Decimal Conversion Tool --------\n"

decInput = int(raw_input("Enter a number to convert: "))

print "\nDecimal = %d" % decInput
print "Binary = %s" % ''.join(binary(decInput))
print "Hexadecimal = %s" % ''.join(hexi(decInput))
print "Octal = %s" % ''.join(octal(decInput))
