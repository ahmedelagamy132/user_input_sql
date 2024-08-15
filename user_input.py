import os
import json
from user_retrive_data import retrive_data

if not os.path.exists("user_data.txt"):
    users_txt = open("user_data.txt", "wt")

while (True):
    print("What do you want to do?")
    print("   1 : Add user")
    print("   2 : Retrive data")
    print("   3 : exit")
    choice = int(input("Enter your choice:"))

    while choice not in [1,2,3]:
        choice = int(input("Enter your choice:"))

    
    if choice == 1:
        userID = str(input("Enter User ID:"))
        firstName = input("Enter First Name:")
        lastName = input("Enter Last Name:")
        age = input("Enter Age:")
        gender = input("Enter Gender:")
        yearOfBirth = input("Enter year Of Birth:")


        while (True):
            if not userID.isalnum():
                userID = str(input("Enter User ID Again:"))
            if not firstName.isalpha():
                firstName = input("Please Enter Your First Name Again:")
            if not lastName.isalpha():
                firstName = input("Please Enter Your Last Name Again:")
            if not age.isnumeric() or int(age) < 18:
                age = input("Please Enter Your Age Again:")
            if gender not in ['Male', 'Female', 'Other']:
                gender = input("Please Enter Gender:")
            if not len(yearOfBirth) == 4 or not age.isnumeric():
                yearOfBirth = input("Please Enter year Of Birth:")
            else:
                break

        print("--------------------------------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------------------------------------")




    try:
        with open("user_data.txt", "r+") as users_txt:
            try:
                user_data = json.load(users_txt)
            except json.JSONDecodeError:
                user_data = {}
            
            if userID in user_data.keys():
                userID = input("This ID is already saved, please choose another ID:")

            new_user_data = {
                userID : {
                    "first_name": firstName,
                    "last_name": lastName,
                    "age": age,
                    "gender": gender,
                    "year_of_birth": yearOfBirth
                    }
                }
           
            user_data.update(new_user_data)
            
            users_txt.seek(0)
            users_txt.truncate()
            
            json.dump(user_data, users_txt, indent=4)
        print("                                       User data has been saved.                                              ")
        print("--------------------------------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------------------------------------")
    except FileNotFoundError:
        print("The file 'user_data.txt' was not found.")
    except PermissionError:
        print("You do not have permission to access 'user_data.txt'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    if choice == 2:
        retrive_data()
        print("--------------------------------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------------------------------------")


    if choice == 3:
        print("Exiting program...")
        exit()
