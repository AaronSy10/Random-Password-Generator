import random
import string

def getletter(): #lower and upper letters
    letters=list(string.ascii_letters) #create list
    letter=random.choice(letters) #choose from list
    return letter #output chosen from list

def getnumber(): #numbers
    numbers=list(string.digits) #create list
    number=random.choice(numbers) #choose from list
    return number #output chosen from list

def getsymbol(): #symbols
    symbols=list(string.punctuation) #create list
    symbol=random.choice(symbols) #choose from list
    return symbol #output chosen from list

def randomize():
    password=list() #create list for password
    while True:
        try:
            i=1
            j=input('Enter the number of characters: ') #get password length
            j=int(j)
            break
        except ValueError:
            print('Invalid input. Please try again.')
    while i<=j:
        counter=random.randrange(0,3) #randomly choose letter,number or symbol
        if counter==0:
            password.append(getletter()) #add to list     
        elif counter==1:
            password.append(getnumber()) #add to list 
        elif counter==2:
            password.append(getsymbol()) #add to list  
        i+=1
    print('Your password is: ',''.join(password)) #output password

randomize()
