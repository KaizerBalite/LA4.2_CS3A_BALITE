# A.1 - Registration
print("=== User Registration ===")
first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
course = input("Enter Course: ")
year_level = input("Enter Year Level: ")
section = input("Enter Section: ")
username = input("Create a Username: ")
password = input("Create a Password: ")

# store details in an array
user_data = [first_name, last_name, course, year_level, section, username, password]

# pinCode validation
while True:
    pin_code = input("Create a 8-digit Pin Code: ")
    if len(pin_code) == 8 and pin_code.isdigit():
        user_data.append(pin_code)
        break
    else:
        print("Pin Code must be exactly 8 digits.")

# A.2 - Registration complete
print("\n Congratulations,", first_name, "! Registration completed.\n")

# A.3 - Ask for login
while True:
    login_choice = input("Do you want to log in? (yes/no): ").lower()
    
    if login_choice == "no":
        print("Goodbye!")
        break

    elif login_choice == "yes":
        while True:
            login_username = input("Enter Username: ")
            login_password = input("Enter Password: ")

            if login_username == user_data[5] and login_password == user_data[6]:
                # A.3.1.2 - Ask for Pin Code
                while True:
                    pin_attempt = input("Enter your 8-digit Pin Code: ")
                    if pin_attempt == user_data[7]:
                        print("\n Login Successful!")
                        print("Here is your registered information:")
                        print(f"Name       : {user_data[0]} {user_data[1]}")
                        print(f"Course     : {user_data[2]}")
                        print(f"Year Level : {user_data[3]}")
                        print(f"Section    : {user_data[4]}")
                        print(f"Username   : {user_data[5]}")
                        break
                    else:
                        print("Incorrect Pin Code. Try again.")

                break  # break from login loop after successful login

            else:
                print("Invalid Username or Password. Please try again.")

        break  # exit the outer login_choice loop after login

    else:
        print("Please enter only 'yes' or 'no'.")