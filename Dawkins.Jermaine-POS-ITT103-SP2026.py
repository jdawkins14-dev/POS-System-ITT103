# -----------------------------------------------------------
# Point of Sale (POS) System
# Author: Jermaine Dawkins
# Course: ITT103
# Description:
# This program simulates a retail Point of Sale system where
# a cashier can add items to a cart, remove items, view the
# cart, checkout customers, and generate receipts.
# -----------------------------------------------------------


# Dictionary storing all products in the store
# Each product contains a price and stock quantity
products = {
    "pyro": {"price": 200.10, "stock": 20},
    "bun": {"price": 150.40, "stock": 15},
    "bakebean": {"price": 120.41, "stock": 25},
    "milk": {"price": 180.22, "stock": 10},
    "bread": {"price": 160.44, "stock": 12},
    "eggs": {"price": 300.50, "stock": 8},
    "juice": {"price": 220.74, "stock": 14},
    "peas": {"price": 100.45, "stock": 18},
    "toothpaste": {"price": 130.14, "stock": 16},
    "water": {"price": 100, "stock": 30}
}

# Dictionary used to store items added to the shopping cart
cart = {}


# -----------------------------------------------------------
# Function to display all available products
# Shows product name, price, and stock quantity
# -----------------------------------------------------------
def display_products():

    print("\nAvailable Products")
    print("-----------------------------------")

    for item, details in products.items():
        print(f"{item} | Price: ${details['price']} | Stock: {details['stock']}")


# -----------------------------------------------------------
# Function to add an item to the shopping cart
# Checks if the product exists and if enough stock is available
# -----------------------------------------------------------
def add_to_cart():

    item = input("Enter product name: ").lower()

    # Check if product exists
    if item not in products:
        print("Product not found.")
        return

    try:
        qty = int(input("Enter quantity: "))

        # Validate quantity input
        if qty <= 0:
            print("Invalid quantity.")
            return

        # Check if enough stock exists
        if qty > products[item]["stock"]:
            print("Not enough stock available.")
            return

        # Add item to cart
        if item in cart:
            cart[item] += qty
        else:
            cart[item] = qty

        # Reduce stock from inventory
        products[item]["stock"] -= qty

        print("Item added to cart.")

    except ValueError:
        print("Invalid input. Please enter a number.")


# -----------------------------------------------------------
# Function to remove an item from the cart
# Restores the item quantity back to stock
# -----------------------------------------------------------
def remove_item():

    item = input("Enter item to remove: ").lower()

    if item in cart:

        # Restore stock quantity
        products[item]["stock"] += cart[item]

        # Remove item from cart
        del cart[item]

        print("Item removed from cart.")

    else:
        print("Item not found in cart.")


# -----------------------------------------------------------
# Function to display items currently in the shopping cart
# Shows quantity and total price for each item
# -----------------------------------------------------------
def view_cart():

    if not cart:
        print("Cart is empty.")
        return

    total = 0

    print("\nShopping Cart")
    print("-----------------------------------")

    for item, qty in cart.items():

        price = products[item]["price"]
        item_total = price * qty

        total += item_total

        print(f"{item} | Qty: {qty} | Total: ${item_total}")

    print("-----------------------------------")
    print(f"Subtotal: ${total}")


# -----------------------------------------------------------
# Function to process checkout
# Calculates subtotal, tax, discount, total, and change
# -----------------------------------------------------------
def checkout():

    if not cart:
        print("Cart is empty.")
        return

    subtotal = 0

    # Calculate subtotal
    for item, qty in cart.items():
        subtotal += products[item]["price"] * qty

    discount = 0

    # Apply discount if subtotal exceeds 5000
    if subtotal > 5000:
        discount = subtotal * 0.05
        print(f"Discount Applied: ${discount}")

    # Calculate tax (10%)
    tax = subtotal * 0.10

    # Calculate final total
    total = subtotal + tax - discount

    print("\n----- BILL -----")
    print(f"Subtotal: ${subtotal}")
    print(f"Tax (10%): ${tax}")
    print(f"Total Amount: ${total}")

    try:

        payment = float(input("Enter amount paid: "))

        # Ensure payment is enough
        while payment < total:
            print("Insufficient payment.")
            payment = float(input("Enter amount again: "))

        change = payment - total

        # Generate receipt
        generate_receipt(subtotal, tax, discount, total, payment, change)

        # Clear cart for next transaction
        cart.clear()

    except ValueError:
        print("Invalid payment amount.")


# -----------------------------------------------------------
# Function to generate a formatted receipt
# Displays items purchased, totals, payment and change
# -----------------------------------------------------------
def generate_receipt(subtotal, tax, discount, total, payment, change):

    print("\n===================================")
    print("         KIND SUPER PLUS STORE")
    print("             RECEIPT")
    print("===================================")

    # Display purchased items
    for item, qty in cart.items():

        price = products[item]["price"]
        item_total = price * qty

        print(f"{item} x{qty} = ${item_total}")

    print("-----------------------------------")

    print(f"Subtotal: ${subtotal}")
    print(f"Tax: ${tax}")
    print(f"Discount: ${discount}")
    print(f"Total: ${total}")
    print(f"Amount Paid: ${payment}")
    print(f"Change: ${change}")

    print("-----------------------------------")
    print("Thank You For Shopping  at KIND SUPER PLUS STORE !")
    print("===================================")


# -----------------------------------------------------------
# Function to display low stock alerts
# Alerts if stock falls below 5 units
# -----------------------------------------------------------
def low_stock_alert():

    for item, details in products.items():

        if details["stock"] < 5:
            print(f"Low stock warning: {item} only {details['stock']} left!")


# -----------------------------------------------------------
# Main program menu
# Allows the cashier to interact with the system
# -----------------------------------------------------------
def main():

    while True:

        print("\n===== POS SYSTEM MENU =====")
        print("1. Display Products")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. View Cart")
        print("5. Checkout")
        print("6. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            display_products()

        elif choice == "2":
            add_to_cart()

        elif choice == "3":
            remove_item()

        elif choice == "4":
            view_cart()

        elif choice == "5":
            checkout()

        elif choice == "6":
            print("System Closed.")
            break

        else:
            print("Invalid option. Please try again.")

        # Check for low stock after each operation
        low_stock_alert()


# Run the POS system
main()
