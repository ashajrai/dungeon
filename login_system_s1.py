
#LOGIN SYSTEM
def Login():
    attempts = 3
    while True:
        while attempts > 0:
            print("===================================")
            print("||WELCOME TO LOG-IN SYSTEM \-.-/||")
            print("===================================")
            choice=input("\n\n1.Register\n2.login\n3.Exit\n\n-------------------------------------------- \nENTER THE NUMBER ACCORDING TO YOUR CHOICE !! \n--------------------------------------------\nSign-In:")

            if choice=="1":
                file = open("users.txt","a")
                file.write(input("Please Register your username:")+":"+input("Please Register your password:")+":"+input("Register your Role:")+"\n")
                file.close()
                print("Registered")

            elif choice=="2":
                username= input("Enter Your Username:")+":"+input("Enter Your Password:")+":"+input("Enter your Role:")+"\n"
                file= open("users.txt","r")
                if username in file.readlines():
                    print("\n\n\n CONGRATULATION!!! YOU'VE LOGGED-IN SUCCESSFULLY (-__-)")
                    return admin_menu()
                else:
                    attempts -= 1
                    print()
                    print("INVALID CREDENTIALS.",{attempts},"ATTEMPTS REMAINING.(^o^)")
                    print()
                    print("HAHAHAHHAHH EXITED FROM THE SYSTEM BYE BYE(^o^)")       
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
            print()
            print("INVALID CHOICE !!!")
            
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
        print("INVALID CHOICE !!!")
        
              

def main():
    print("\n\n\n||||||||||||||||||||||||||||||||||||||||||||||")
    print("WELCOME TO MALAYSIAN RESTAURANT,KUALA LYAMPUR")
    print("||||||||||||||||||||||||||||||||||||||||||||||\n\n")
    username, role=Login()
    if role == "admin":
        admin_menu()

if __name__ == "__main__":        
    main()
