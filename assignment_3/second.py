# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is______.

def getapp():
   app= int (input('How many apples do you want to buy?: '))
   return app

def getore():
    ore= int (input ('How many oranges do you want to buy: '))
    return ore

def totalapp():
    price_app= 20
    return (apples* price_app)

def totalore():
    price_ore=25
    return (oranges* price_ore)
    

def display(totalF):
    print (f"the total amount is {totalF}")
    
    

#steps
# ask how many apples you want to buy
apples = getapp()
# ask how many oranges you want to buy
oranges = getore()
# multiply the amount of apples with the price 20 peso
totalApp= totalapp()
#multiply the amount of orange to the price 25 peso
totalOre= totalore()
# add the total amounts of apple and orange
total= totalOre + totalApp
# display total amount
display(total)