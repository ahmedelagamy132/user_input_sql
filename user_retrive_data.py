import json
def retrive_data(): 
    with open("user_data.txt", 'r') as users:
        users_data = json.load(users)

    print("What do you want to retrive?")
    print("   1 : All the Data")
    print("   2 : Specific User by ID")
    print("   3 : exit")
    choice = int(input("Enter your choice:"))

    while choice not in [1,2,3]:
        choice = input("Enter your choice:")
    if choice == 1:
        for i in users_data.keys():
            print(i ,":",users_data[i], end=",\n")

    if choice == 2:
        user_id = input("Enter User Id:")

        userById = users_data[user_id]
        print(userById)

    if choice == 3:
        exit()