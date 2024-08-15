import mysql.connector
import json

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ae13200456*",
    database="UserDatabase"
)

cursor = db_connection.cursor()



with open("user_data.txt", "r") as users:
    users_data = json.load(users)

for key, user in users_data.items():
    try:
        insert_query = """
                INSERT INTO Users (user_id, first_name, last_name, age, gender, year_of_birth)
                VALUES (%s, %s, %s, %s, %s, %s)
            """
        values = (
            key,
            user.get('first_name'),
            user.get('last_name'),
            user.get('age'),
            user.get('gender'),
            user.get('year_of_birth')
        )

        cursor.execute(insert_query, values)

        # print(key, user)
        # fname = user.get('first_name')
        # print(fname)


        db_connection.commit()

        print("Data inserted successfully!")

    except mysql.connector.errors.IntegrityError as ie: 
        if ie.errno == 1062:
            print("Duplicate entry error", ie)
        else:
            print("IntegrityError occurred: ", ie)
    
    except mysql.connector.Error as e:
        print("MySQL Error: ", e)
    except Exception as e:
        print("An error occurred: ", e)

    finally:
        cursor.close()
        db_connection.close()