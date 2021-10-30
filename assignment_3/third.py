#Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
#Display the maximum number of apples that you can buy and the remaining money that you will have.
#Display the output in the following format.
#You can buy ___ apples and your change is ___ pesos.

def getmoney():
    Money= int (input('Enter amount of money: '))
    return Money

def getprice():
    Priceapp= int (input ('price of apple:'))
    return Priceapp

def getmax_app():
    max_app= money // price
    return max_app

def getchange():
    Change= money - max * price
    return Change

def display(maxF, changeF):
    print (f"You can buy {maxF} apples and your change is {change} pesos")

    
    

#steps
#Enter the amount of money
money= getmoney()
#Enter the price of apple
price= getprice()
#Get the max number of apples you can buy
max = getmax_app()
#Get the change
change= getchange()
#display the amount
display(max,change)