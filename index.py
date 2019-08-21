# exercise 1
#Create two variables. One should equal “My name is: “ 
# and the other should equal your actual name. 
# Print the two variables in one print mess
# name = ('My name is: ')
# 
# first = ('Dekevion')
# 
# sentence = print(name + first)


# exercise 2 
# Ask the user to enter the extra credit they earned. 
# If they entered less than 5 print “That’s not enough extra credit.” 
# If they entered more than 20 print “That’s too much extra credit”.
# 
# askForCredit = int(input("Enter the extra credit earned"))
# 
# if askForCredit < 5:
#     print('not enough extra credit')
# elif askForCredit > 20:
#     print ('too much extra credit')
#     
# exercise 3
#Ask a user to enter a password. Enter a password. 
# Ask user to reenter password. Check to see if they are correct.

# askForPassword = input('enter password')
# 
# reenter = input('reenter password')
# 
# if askForPassword is reenter:
#     print('correct')

#exercise 4
#Ask for two card numbers. If it equals 21 print BLACKJACK!, 
# if it’s greater than 21 print BUST!, 
# if it’s less than 21 print “The total is [THE TOTAL]”

cardNum = int(input("Card number?"))

cardNum2 = int(input("Card number?"))

sumOfCards = (cardNum + cardNum2)

if sumOfCards is 21:
    print('BLACKJACK!')
if sumOfCards > 21:
    print ("BUST")
elif sumOfCards < 21:
    print ('The total is ' + (str)(sumOfCards))
          


