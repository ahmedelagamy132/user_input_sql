
# User Data Management Project

This project allows you to manage user data through a simple command-line interface. Users can add new data, retrieve existing data, and migrate data from a text file to a MySQL database.

## Project Structure

- **user_input.py**: This is the main file of the project that handles adding users, retrieving data, and interacting with the user.
- **user_retrive_data.py**: This file contains the `retrive_data` function, which is used to retrieve user data from the text file.
- **mysql_connection.pyg**: This script is responsible for migrating user data from a text file to a MySQL database.

## Setup

### Prerequisites

- Python 3.x
- MySQL Server
- MySQL Connector for Python

### Installation

1. Clone the repository:
   ```bash
   git clone [https://github.com/yourusername/user-data-management.git](https://github.com/ahmedelagamy132/user_input_sql.git)
   cd user-data-management
   ```

2. Install the necessary Python packages:
   ```bash
   pip install mysql-connector-python
   ```

3. Set up your MySQL database:
   - Create a database named `UserDatabase`.
   - Create a table named `Users` with the following schema:
     ```sql
     CREATE TABLE Users (
       user_id VARCHAR(255) PRIMARY KEY,
       first_name VARCHAR(255),
       last_name VARCHAR(255),
       age INT,
       gender VARCHAR(255),
       year_of_birth INT
     );
     ```

4. Update the MySQL connection credentials in `mysql_connection.py`:
   ```python
   db_connection = mysql.connector.connect(
       host="localhost",
       user="your_mysql_username",
       password="your_mysql_password",
       database="UserDatabase"
   )
   ```

## Usage

### Running the Application

- Execute the `user_input.py` script to start managing user data:
  ```bash
  python user_input.py
  ```

### Migrating Data to MySQL

- Run the `mysql_connection.py` script to migrate data:
  ```bash
  python mysql_connection.py
  ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with any improvements.

## Contact

For any inquiries or issues, feel free to reach out to [ahmedelagamy132@example.com](mailto:ahmedelagamy132@example.com).
