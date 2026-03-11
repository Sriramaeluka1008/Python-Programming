#     User Interaction:
    #     #The system should ask for the customer’s name.
    #     #Display a list of available products with their prices.
    #     Allow users to add multiple items to their cart.
    #     Validate that the quantity entered is a valid number.
    #     Display an itemized bill with total and tax before exiting.

    # #Product Catalog:
    #     Maintain a dictionary of products and their prices.
    #     Display the product list when requested.

    # Billing and Calculations:
    #     Compute the total price based on item quantities.
    #     Apply a 12% tax on the total amount.
    #     Display a detailed invoice with:
    #         Item name
    #         Quantity
    #         Price per unit
    #         Total price for each item
    #         Total amount before and after tax

    # Receipt Format:
    #     Display a well-formatted bill with store name, location, and transaction details.

    # Exit Mechanism:
    #     Allow users to exit the purchase process at any time.
    #     Display a "Thank you" message upon exiting.

# Supermarket Billing System 

products = {
    1: ("Rice", 149),
    2: ("Sugar", 45),
    3: ("Milk", 40),
    4: ("Bread", 35),
    5: ("Eggs", 6)
}

TAX = 0.12

print("===== Welcome to D MART =====")
customer = input("Enter Customer Name: ")

cart = {}
subtotal = 0

while True:
    print("\nAvailable Products:")
    for key, value in products.items():
        print(key, "-", value[0], "₹", value[1])

    print("6 - Exit")

    choice = int(input("Select product number: "))

    if choice == 6:
        break

    if choice in products:
        quantity = input("Enter quantity: ")

        if not quantity.isdigit():
            print("Invalid quantity! Try again.")
            continue

        quantity = int(quantity)
        name, price = products[choice]

        total_price = price * quantity
        subtotal += total_price

        if name in cart:
            cart[name] += quantity
        else:
            cart[name] = quantity

        print(f"{name} added successfully!")
    else:
        print("Invalid choice!")


tax_amount = subtotal * TAX
grand_total = subtotal + tax_amount

print("\n========== RECEIPT ==========")
print("D MART")
print("Location: WARANGAL")
print("Customer:", customer)
print("------------------------------")

for item, qty in cart.items():
    print(f"{item} x{qty}")

print("------------------------------")
print("Subtotal:", subtotal)
print("Tax (12%):", tax_amount)
print("Grand Total:", grand_total)
print("------------------------------")
from datetime import datetime
print(datetime.now())
print("Thank you! Visit Again!")
