import os
import json
from user_retrive_data import retrive_data  # Importing the retrieve_data function from another module

# Check if the user data file exists, create it if it doesn't
if not os.path.exists("user_data.txt"):
    users_txt = open("user_data.txt", "wt")

while True:
    # Display the menu options to the user
    print("What do you want to do?")
    print("   1 : Add user")
    print("   2 : Retrieve data")
    print("   3 : Exit")
    choice = int(input("Enter your choice:"))

    # Validate user choice
    while choice not in [1, 2, 3]:
        choice = int(input("Enter your choice:"))

    if choice == 1:
        # Gather user information
        userID = str(input("Enter User ID:"))
        firstName = input("Enter First Name:")
        lastName = input("Enter Last Name:")
        age = input("Enter Age:")
        gender = input("Enter Gender:")
        yearOfBirth = input("Enter Year Of Birth:")

        # Validate user inputs
        while True:
            if not userID.isalnum():
                userID = str(input("Enter User ID Again:"))
            if not firstName.isalpha():
                firstName = input("Please Enter Your First Name Again:")
            if not lastName.isalpha():
                lastName = input("Please Enter Your Last Name Again:")
            if not age.isnumeric() or int(age) < 18:
                age = input("Please Enter Your Age Again:")
            if gender not in ['Male', 'Female', 'Other']:
                gender = input("Please Enter Gender:")
            if not len(yearOfBirth) == 4 or not age.isnumeric():
                yearOfBirth = input("Please Enter Year Of Birth:")
            else:
                break

        # Save the validated user data to the file
        try:
            with open("user_data.txt", "r+") as users_txt:
                try:
                    user_data = json.load(users_txt)
                except json.JSONDecodeError:
                    user_data = {}

                # Ensure unique user ID
                if userID in user_data.keys():
                    userID = input("This ID is already saved, please choose another ID:")

                # Prepare new user data
                new_user_data = {
                    userID: {
                        "first_name": firstName,
                        "last_name": lastName,
                        "age": age,
                        "gender": gender,
                        "year_of_birth": yearOfBirth
                    }
                }

                # Update and save the data
                user_data.update(new_user_data)
                users_txt.seek(0)
                users_txt.truncate()
                json.dump(user_data, users_txt, indent=4)

            print("User data has been saved.")

        except FileNotFoundError:
            print("The file 'user_data.txt' was not found.")
        except PermissionError:
            print("You do not have permission to access 'user_data.txt'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    elif choice == 2:
        # Call the retrieve data function from the imported module
        retrive_data()

    elif choice == 3:
        # Exit the program
        print("Exiting program...")
        exit()
