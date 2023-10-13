#need to do file saving and calling 



accuracy = 0
bags = 0
total = 0
totalbags = 0
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

volunteer = {
    "name1": 0,
    "total1": 0,
    "totalbags1": 0,
    "accuracy1": 0,
}

name=input("What is your name? ")

volunteer.update({"name1":name})

bags = int(input("How many bags do you have to input? "))

while bags > 0:
    bags = bags - 1
    coin=input("What coin type do you have? ")
    weight=int(input("How much does the bag weigh? "))

        
    if coin not in coinweights:
        print("Invaild coin type")
    else:
        print("Valid coin type")

    actual_weight = bagweight[coin]

    total += bagvalue[coin]
    totalbags = totalbags + 1

    if actual_weight > weight:
        print("you need to add ",actual_weight - weight,"g")
        accuracy = totalbags - 1
    if actual_weight < weight:
        print("you need to remove",weight - actual_weight,"g")
        accuracy = totalbags - 1

accuracy
        

show = input("Would you like to show your total of bags, total value and accuracy? y/n ")
if show == ("y"):
        print("Your total bags is now",totalbags)
        print("your total for",name, "is now £",total)
        print("You have inputed ",accuracy, "/", totalbags,"total bags wrong.") 

volunteer.update({"totalbags1":totalbags})
volunteer.update({"total1":total})
volunteer.update({"accuracy1":accuracy})

print(volunteer)
