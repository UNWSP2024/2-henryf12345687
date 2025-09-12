# Henry Forst 
#09/10/25
# Assignment 2
def calculate_total_purchase():
    # A customer in a store is purchasing five items.  
    # Write a program that asks for each item, 
    item1 = input("What is your first item? ")
    item2 = input("What is your second item? ")
    item3 = input("What is your third item? ")
    item4 = input("What is your fourth item? ")
    item5 = input("What is your fifth item? ")
    # then displays the subtotal of the sale, 
def calculate_subtotal():
    cost1 = int(input("What does the first item cost? "))
    cost2 = int(input("What does your second item cost? "))
    cost3 = int(input("What does your third item cost? "))
    cost4 = int(input("What does your fourth item cost? "))
    cost5 = int(input("What does your fifth item cost? "))
    subtotal = cost1 + cost2 + cost3 + cost4 + cost5
    print("Your subtotal is:", subtotal , "Dollars")
    # the amount of sales tax, and the total.  
    tax = subtotal * .07
    print("Your tax is:", tax)
    total = tax + subtotal
    print("Your total is:", total, "Dollars")
    # Assume the sales tax is 7 percent.

calculate_total_purchase()
calculate_subtotal()
