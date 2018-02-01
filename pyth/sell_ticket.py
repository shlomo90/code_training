'''
This program is selling a ticket.
if you input an age, make a decision it's possible or not to sell ticket.
'''

age = 3

if (age > 18 and age < 80):
    print('you can buy this ticket.')
elif (age < 18) :
    print('no it\'s impossible.')
else:
    print('you are too old')
