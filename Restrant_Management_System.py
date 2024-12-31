#Restro Management System

#Item in restro in Value of Dict
Food_Item ={
    "PIZZA" : 299,
    "BARGAR" : 149,
    "COFFEE" : 149,
    "COKE" : 40,
    "GARLICK BRADE" : 499,
    "SALARD" : 40,
}

#TEXT
print("Thear IS Your Food Menu Cart")
print("PIZZA : MRP299\nBARGAR : MRP149\nCOFFEE : MRP149\nCOKE : MRP40\nGARLICK BRADE : MRP499\nSALARD : MRP40")

#ODER_FOOD Item Is in a value
print(" \n ")
Oder_Food = (input("Odear pliese : "))
Bill = 0
Total = 0
#Conditions
if Oder_Food in Food_Item:
    print("Your Order Done .....")
    Bill = Food_Item[Oder_Food]
    Addone_bill = Food_Item[Oder_Food]
    print(f"Heare Is Your Oder : {Oder_Food} MRP : {Addone_bill}""\n ")
    Total = Bill

    #Second Oder Condition 
    ADD = str(input("You Want To Add Anather Item : "))
#Mainframe Calculation and Oder Bill Or Pament Result
    if ADD == "yes":
        Second_Oder = str(input("Oder Please : "))
        Bill_2 = Food_Item[Second_Oder]
        Total += Bill_2
    else:
        pass
else:
    print("Your Orders Is Not Availavil At This Moment")
    Total = Bill
    print("Wait....\n")

print("Your Total Bill:" ,"MRP ",Total,)
print("Pay The Bill Thank You To Visit My Small Project")