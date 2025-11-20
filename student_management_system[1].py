# Student Management System
# Assignment - 2 (Student Registration System)

students = {}
curr_user = None


def register():
    print(" Register")
    username = input(" Enter Username: ")

    if username in students:
        print("Username already exists.")
        return

    password = input(" Enter Password: ")
    full_name = input(" Enter Full Name: ")
    email = input(" Enter Email: ")
    phoneno = input(" Enter Phone Number: ")
    dob = input(" Date of Birth: ")
    gender = input(" Gender: ")
    address = input(" Enter your Address: ")
    course = input(" Course: ")
    year = input(" Year of Study: ")
    student_id = input(" Student ID: ")

    students[username] = {
        "username": username,
        "password": password,
        "full_name": full_name,
        "email": email,
        "phone": phoneno,
        "dob": dob,
        "gender": gender,
        "address": address,
        "course": course,
        "year": year,
        "student_id": student_id,
    }

    print("Registration successfully Done.")


def login():
    global curr_user
    print(" Login ")
    username = input(" Username: ")
    password = input(" Password: ")

    if username in students and students[username]["password"] == password:
        curr_user = username
        print(f"welcome, {students[username]['full_name']}!")
    else:
        print("invalid username or password.")


def show_profile():
    if curr_user is None:
        print("You must be logged in.")
        return

    print(" Profile ")
    for key, value in students[curr_user].items():
        if key != "password":
            print(f"{key.replace('_', ' ').title()}: {value}")


def update_profile():
    if curr_user is None:
        print(" You must be logged in.")
        return

    print(" Update Profile ")
    user = students[curr_user]

    for key in user:
        if key not in ["username", "password"]:
            new_val = input(f"{key.replace('_', ' ').title()} [{user[key]}]: ")
            if new_val.strip():
                user[key] = new_val

    change_password = input("Do you want to change your password? (y/n): ").lower()
    if change_password == "y":
        new_pass = input(" Enter new Password: ")
        user["password"] = new_pass
        print(" Now Password updated.")

    print("Profile updated.")


def logout():
    global curr_user
    if curr_user:
        print(f"Logged out from {curr_user}")
        curr_user = None
    else:
        print("No user is currently logged in.")


def exit_program():
    print(" Exiting system!")
    return "exit"


def main():
    while True:
        print("\n Student Management System ")
        print("1. Register")
        print("2. Login")
        print("3. Show Profile")
        print("4. Update Profile")
        print("5. Logout")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            show_profile()
        elif choice == "4":
            update_profile()
        elif choice == "5":
            logout()
        elif choice == "6":
            result = exit_program()
            if result == "exit":
                break
        else:
            print("Invalid option. Please enter a number from 1 to 6.")


main()

