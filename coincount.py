bags = 0
total = 0
coinweights = {
    "£2": 12.00,
    "£1": 8.75,
    "50p": 8.00,
    "20p": 5.00,
    "10": 6.50,
    "5p": 2.35,
    "2p": 7.12,
    "1p": 3.56,
    }


bagvalue = {
    "£2": 20,
    "£1": 20,
    "50p": 10,
    "20p": 10,
    "10": 5,
    "5p": 5,
    "2p": 1,
    "1p": 1,
}


bagweight = {
    "£2": 120,
    "£1": 175,
    "50p": 160,
    "20p": 250,
    "10": 325,
    "5p": 235,
    "2p": 356,
    "1p": 356,
}


name=input("What is your name? ")

coin=input("What coin type do you have? ")

weight=int(input("How much does the bag weigh "))
#need to make it repeatable 

if coin not in coinweights:
    print("Invaild coin type")
else:
    print("Valid coin type")

actual_weight = bagweight[coin]

if actual_weight > weight:
    print("you need to add ",actual_weight - weight,"g")
if actual_weight < weight:
    print("you need to remove",weight - actual_weight,"g")
#need to add so u cant input words 


show = input("Would you like to show your total of bags and total value? y/n ")
if show == ("y"):
    if actual_weight == weight: 
        bags += 1
        print("Your total bags is now",bags)

    if actual_weight == weight:
        total += bagvalue[coin]
        print ("your total for",name, "is now £",total)

