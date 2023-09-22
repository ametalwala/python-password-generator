import random 

# Welcome statement, greets user upon running script
print('Welcome To Your Password Generator')

# setting character options for randomizer"
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@$#%&^*().,?0123456789"

# sets requirements for amount of passwords to generate 
# converts input response into integer, allowing for text comprehension
number = input('Amount of passwords to generate: ')
number = int(number)

# sets requirements for length of passwords 
# converts input to integer as above 
length = input('Input your password length: ')
length = int(length)

# statement to present passwords 
print('\nhere are your passwords: ')

# implementing for loop to initiate randomizer to create passwords 
for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)