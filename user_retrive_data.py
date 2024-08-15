import json

def retrive_data():
    # Open the user data file and load its content
    with open("user_data.txt", 'r') as users:
        users_data = json.load(users)

    # Display the menu options for retrieving data
    print("What do you want to retrieve?")
    print("   1 : All the Data")
    print("   2 : Specific User by ID")
    print("   3 : Exit")
    choice = int(input("Enter your choice:"))

    # Validate user choice
    while choice not in [1, 2, 3]:
        choice = input("Enter your choice:")

    if choice == 1:
        # Print all user data
        for i in users_data.keys():
            print(i, ":", users_data[i], end=",\n")

    elif choice == 2:
        # Retrieve specific user data by ID
        user_id = input("Enter User ID:")
        if user_id in users_data:
            userById = users_data[user_id]
            print(userById)
        else:
            print("User ID not found.")

    elif choice == 3:
        # Exit the function
        exit()
