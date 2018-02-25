import sys

first_number = raw_input("What is the first number?")

'''
just in case that input is below zero, We should use the function int()
for checking correctly.
'''

if (first_number.isdigit() is False):
    print("first_number is not digit")
    sys.exit(1)

second_number = raw_input("What is the second number?")
if (second_number.isdigit() is False):
    print("second_number is not digit")
    sys.exit(1)

if (second_number == '0'):
    print("second_number must not be zero")
    sys.exit(1)

print(first_number + ' + ' + second_number + ' = ' +
      str(int(first_number) + int(second_number)))

print(first_number + ' - ' + second_number + ' = ' +
      str(int(first_number) - int(second_number)))

print(first_number + ' * ' + second_number + ' = ' +
      str(int(first_number) * int(second_number)))

print(first_number + ' / ' + second_number + ' = ' +
      str(int(first_number) / int(second_number)))
