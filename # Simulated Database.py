# Simulated Database
users = {
    "admin": {"password": "admin123", "role": "Admin"},
    "manager": {"password": "manager123", "role": "Manager"},
    "chef": {"password": "chef123", "role": "Chef"},
    "customer": {"password": "customer123", "role": "Customer"}
}

staff = {
    "manager1": {"name": "John Doe", "role": "Manager"},
    "chef1": {"name": "Jane Doe", "role": "Chef"}
}

customers = {
    "customer1": {"name": "Alice", "contact": "123456789"}
}

menu = {
    "1": {"name": "Nasi Lemak", "category": "Malaysian", "price": 10},
    "2": {"name": "Chicken Rice", "category": "Chinese", "price": 8},
    "3": {"name": "Butter Chicken", "category": "Indian", "price": 12},
    "4": {"name": "Hokkein Mee", "category": "Chinese", "price": 8},
    "5": {"name": "Redang", "category": "Malaysian", "price": 8}
}

orders = {}
feedback = []
ingredients = []

# Login Function
def login():
    attempts = 3
    while attempts > 0:
        username = input("Enter username: ")
        password = input("Enter password: ")
        if username in users and users[username]["password"] == password:
            print(f"Login successful! Welcome, {username}.")
            return username, users[username]["role"]
        else:
            attempts -= 1
            print(f"Invalid credentials. {attempts} attempts remaining.")
    print("Too many failed attempts. Exiting.")
    exit()

# Admin Functions
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Manage Staff")
        print("2. View Sales Report")
        print("3. View Feedback")
        print("4. Update Profile")
        print("5. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            manage_staff()
        elif choice == "2":
            view_sales_report()
        elif choice == "3":
            view_feedback()
        elif choice == "4":
            update_profile()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def manage_staff():
    print("\nManage Staff:")
    print("1. Add Staff")
    print("2. Edit Staff")
    print("3. Delete Staff")
    choice = input("Enter choice: ")
    if choice == "1":
        staff_id = input("Enter staff ID: ")
        name = input("Enter name: ")
        role = input("Enter role (Manager/Chef): ")
        staff[staff_id] = {"name": name, "role": role}
        print("Staff added successfully.")
    elif choice == "2":
        staff_id = input("Enter staff ID to edit: ")
        if staff_id in staff:
            name = input("Enter new name: ")
            role = input("Enter new role: ")
            staff[staff_id] = {"name": name, "role": role}
            print("Staff updated successfully.")
        else:
            print("Staff not found.")
    elif choice == "3":
        staff_id = input("Enter staff ID to delete: ")
        if staff_id in staff:
            del staff[staff_id]
            print("Staff deleted successfully.")
        else:
            print("Staff not found.")
    else:
        print("Invalid choice.")

def view_sales_report():
    print("\nSales Report:")
    # Simulated sales data
    print("Total Sales: $1000")

def view_feedback():
    print("\nCustomer Feedback:")
    for fb in feedback:
        print(fb)

def update_profile():
    print("\nUpdate Profile:")
    # Simulated profile update
    print("Profile updated successfully.")

# Manager Functions
def manager_menu():
    while True:
        print("\nManager Menu:")
        print("1. Manage Customers")
        print("2. Manage Menu")
        print("3. View Ingredients")
        print("4. Update Profile")
        print("5. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            manage_customers()
        elif choice == "2":
            manage_menu()
        elif choice == "3":
            view_ingredients()
        elif choice == "4":
            update_profile()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def manage_customers():
    print("\nManage Customers:")
    print("1. Add Customer")
    print("2. Edit Customer")
    print("3. Delete Customer")
    choice = input("Enter choice: ")
    if choice == "1":
        customer_id = input("Enter customer ID: ")
        name = input("Enter name: ")
        contact = input("Enter contact: ")
        customers[customer_id] = {"name": name, "contact": contact}
        print("Customer added successfully.")
    elif choice == "2":
        customer_id = input("Enter customer ID to edit: ")
        if customer_id in customers:
            name = input("Enter new name: ")
            contact = input("Enter new contact: ")
            customers[customer_id] = {"name": name, "contact": contact}
            print("Customer updated successfully.")
        else:
            print("Customer not found.")
    elif choice == "3":
        customer_id = input("Enter customer ID to delete: ")
        if customer_id in customers:
            del customers[customer_id]
            print("Customer deleted successfully.")
        else:
            print("Customer not found.")
    else:
        print("Invalid choice.")

def manage_menu():
    print("\nManage Menu:")
    print("1. Add Menu Item")
    print("2. Edit Menu Item")
    print("3. Delete Menu Item")
    choice = input("Enter choice: ")
    if choice == "1":
        item_id = input("Enter item ID: ")
        name = input("Enter name: ")
        category = input("Enter category: ")
        price = float(input("Enter price: "))
        menu[item_id] = {"name": name, "category": category, "price": price}
        print("Menu item added successfully.")
    elif choice == "2":
        item_id = input("Enter item ID to edit: ")
        if item_id in menu:
            name = input("Enter new name: ")
            category = input("Enter new category: ")
            price = float(input("Enter new price: "))
            menu[item_id] = {"name": name, "category": category, "price": price}
            print("Menu item updated successfully.")
        else:
            print("Menu item not found.")
    elif choice == "3":
        item_id = input("Enter item ID to delete: ")
        if item_id in menu:
            del menu[item_id]
            print("Menu item deleted successfully.")
        else:
            print("Menu item not found.")
    else:
        print("Invalid choice.")

def view_ingredients():
    print("\nIngredients List:")
    for ing in ingredients:
        print(ing)

# Chef Functions
def chef_menu():
    while True:
        print("\nChef Menu:")
        print("1. View Orders")
        print("2. Update Order Status")
        print("3. Request Ingredients")
        print("4. Update Profile")
        print("5. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            view_orders()
        elif choice == "2":
            update_order_status()
        elif choice == "3":
            request_ingredients()
        elif choice == "4":
            update_profile()
        elif choice == "5":
            break
        else:
            print("Invalid choice.")

def view_orders():
    print("\nOrders:")
    for order_id, details in orders.items():
        print(f"Order ID: {order_id}, Details: {details}")

def update_order_status():
    order_id = input("Enter order ID: ")
    if order_id in orders:
        status = input("Enter new status (In Progress/Completed): ")
        orders[order_id]["status"] = status
        print("Order status updated successfully.")
    else:
        print("Order not found.")

def request_ingredients():
    ingredient = input("Enter ingredient: ")
    ingredients.append(ingredient)
    print("Ingredient requested successfully.")

# Customer Functions
def customer_menu():
    while True:
        print("\nCustomer Menu:")
        print("1. View Menu")
        print("2. Place Order")
        print("3. View Order Status")
        print("4. Send Feedback")
        print("5. Update Profile")
        print("6. Logout")
        choice = input("Enter choice: ")
        if choice == "1":
            view_menu()
        elif choice == "2":
            place_order()
        elif choice == "3":
            view_order_status()
        elif choice == "4":
            send_feedback()
        elif choice == "5":
            update_profile()
        elif choice == "6":
            break
        else:
            print("Invalid choice.")

def view_menu():
    print("\nMenu:")
    for item_id, details in menu.items():
        print(f"ID: {item_id}, Name: {details['name']}, Category: {details['category']}, Price: ${details['price']}")

def place_order():
    view_menu()
    item_id = input("Enter item ID to order: ")
    if item_id in menu:
        order_id = str(len(orders) + 1)
        orders[order_id] = {"item": menu[item_id]["name"], "status": "Pending"}
        print("Order placed successfully.")
    else:
        print("Item not found.")

def view_order_status():
    order_id = input("Enter order ID: ")
    if order_id in orders:
        print(f"Order Status: {orders[order_id]['status']}")
    else:
        print("Order not found.")

def send_feedback():
    fb = input("Enter feedback: ")
    feedback.append(fb)
    print("Feedback submitted successfully.")

# Main Program
def main():
    print("-------------------------------------------------------")
    print("|| Welcome to Delicious Restaurant Management System ||")
    print("=======================================================")
    username, role = login()
    if role == "Admin":
        admin_menu()
    elif role == "Manager":
        manager_menu()
    elif role == "Chef":
        chef_menu()
    elif role == "Customer":
        customer_menu()

if __name__ == "__main__":
    main()