from datetime import datetime

# In-memory storage for admin credentials
admin_credentials = {
    "username": "admin",  # Replace with your desired default username
    "password": "password"  # Replace with your desired default password
}

# In-memory menu
menu = {
    "Idli": 10,
    "Dosa": 32,
    "Roti": 7,
    "Rice": 12,
    "Dal": 12
}

# In-memory storage for bills
bills = []

def signup():
    new_username = input("Enter new username: ")
    new_password = input("Enter new password: ")
    admin_credentials["username"] = new_username
    admin_credentials["password"] = new_password
    print("Signup successful! You can now log in with your new credentials.")

def reset_password():
    current_username = admin_credentials["username"]
    current_password = admin_credentials["password"]

    username = input("Enter current username: ")
    password = input("Enter current password: ")

    if username == current_username and password == current_password:
        new_password = input("Enter new password: ")
        admin_credentials["password"] = new_password
        print("Password successfully updated!")
    else:
        print("Invalid current username or password.")

def login():
    retries = 3
    while retries > 0:
        username = input("Enter Username: ")
        password = input("Enter Password: ")
        if username == admin_credentials["username"] and password == admin_credentials["password"]:
            print("Login successful!")
            return True
        else:
            retries -= 1
            print(f"Incorrect credentials. You have {retries} retry/ies left.")
    
    print("Login failed. You have exceeded the number of retries.")
    return False

def choose_payment_method():
    print("Choose mode of payment:")
    print("1. UPI")
    print("2. Debit Card")
    print("3. Credit Card")
    print("4. Cash")
    
    while True:
        choice = int(input("Enter your choice: "))
        if choice == 1:
            return "UPI"
        elif choice == 2:
            return "Debit Card"
        elif choice == 3:
            return "Credit Card"
        elif choice == 4:
            return "Cash"
        else:
            print("Invalid choice. Please select again.")

def print_bill(bill):
    # Displaying bill details
    print("\nGenerated Bill:")
    print("........................................")
    print(f".............BILL NUMBER: {bill['bill_number']}...........")
    print(f"WELCOME {bill['customer_name']}      {bill['date']}")
    print("........................................")
    print("                  BILL                  ")
    print("........................................")
    print("|    ITEM    |     COST    |     QTY   |")
    print("........................................")
    for i, item in enumerate(bill["items"], start=1):
        print(f"{i}.    {item['name']}     {item['price']}      {item['quantity']}")
    print("........................................")
    print(f"                          TOTAL: {bill['total']}")
    print(f"               TAX (20 Percent): {round(bill['tax'])}")
    print(f"                    GRAND TOTAL: {bill['grand_total']}")
    print(f"             MODE OF PAYMENT: {bill['payment_method']}")
    print("........................................")
    print("               |THANK YOU!|             ")
    print("      |YOUR ORDER HAS BEEN PLACED!|     ")
    print("........................................")

def show_bills_for_customer(customer_name):
    print(f"\nShowing previous bills for {customer_name}:")
    bills_found = False
    for bill in bills:
        if bill['customer_name'].lower() == customer_name.lower():
            print("\n----------------------")
            print_bill(bill)
            print("----------------------")
            bills_found = True
    if not bills_found:
        print("No bills found for this customer.")

def take_order():
    # Taking customer order
    name = input("Enter Name: ")

    # Generating bill number
    bill_number = len(bills) + 1

    # Creating bill template
    bill = {
        "bill_number": bill_number,
        "customer_name": name,
        "date": datetime.now().strftime('%d/%m/%Y %H:%M:%S'),
        "items": [],
        "total": 0,
        "tax": 0,
        "grand_total": 0,
        "payment_method": ""
    }

    # Displaying the menu
    print("Here is the Menu\n................")
    for item, price in menu.items():
        print(f"{item} - Rs {price}")

    # Taking orders
    while True:
        item_name = input("Enter item name (type 'quit' to exit): ").title()
        if item_name.lower() == 'quit':
            break
        if item_name in menu:
            quantity = int(input("Enter Quantity: "))
            price = menu[item_name]
            bill["items"].append({"name": item_name, "price": price, "quantity": quantity})
            bill["total"] += price * quantity
        else:
            print("Item not found in menu.")

    # Calculating tax and grand total
    bill["tax"] = 0.2 * bill["total"]
    bill["grand_total"] = bill["total"] + bill["tax"]

    # Choose payment method
    bill["payment_method"] = choose_payment_method()

    # Adding bill to the list of bills
    bills.append(bill)

    # Prompt to print the bill
    print("Do you want to print the bill?")
    print("1. Yes")
    print("2. No")
    
    print_choice = int(input("Enter your choice: "))
    if print_choice == 1:
        print_bill(bill)
    else:
        print("Bill not printed.")

def main():
    while True:
        print("WELCOME:")
        print("1. Login")
        print("2. Sign Up")
        print("3. Reset Password")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            if login():
                break  # Exit the loop and proceed to the main functionality

        elif choice == 2:
            signup()

        elif choice == 3:
            reset_password()

        elif choice == 4:
            print("Exiting...")
            return

        else:
            print("Invalid choice")

    while True:
        print("ADMIN MENU:")
        print("1. Take New Order")
        print("2. Show Previous Orders")
        print("3. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            take_order()

        elif choice == 2:
            customer_name = input("Enter the name of the customer to view previous bills: ")
            show_bills_for_customer(customer_name)

        elif choice == 3:
            print("Exiting...")
            break

        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
