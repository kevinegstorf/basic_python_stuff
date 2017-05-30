# This program says hello and asks for my name

print('Hello World!')
print('What is your name')
myName = input()
print ('It is nice to meet you, ' + myName.capitalize() + '!')
print('the length of your name is:' )
print(len(myName))
print('How old are you?')
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year.')
