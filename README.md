# MySQL Command Line Interface

## Overview
This Python script is a simple MySQL command-line interface that allows users to connect to a MySQL server, view available databases, select a database, and execute SQL commands interactively.

## Features
- Connect to a MySQL server using provided credentials.
- List all user databases (excluding system databases).
- Allow the user to select a database to interact with.
- Execute SQL commands (e.g., SELECT, INSERT, UPDATE, DELETE) directly on the selected database.
- Display query results in a table-like format.

## Installation

1. Ensure you have Python 3.6 or higher installed on your machine.
2. Install the MySQL Connector package:

``` bash
pip install mysql-connector-python
```

## Usage
To run the script, execute the following command in your terminal:
```bash
python mysql_cli.py <host> <user> <password>
```
Replace <host> with the MySQL server host (IP or domain name), <user> with your MySQL username, and <password> with your MySQL password. For example:

``` bash
python mysql_cli.py 127.0.0.1 root mypassword
```


## Script Workflow
<ol>
<li>The script connects to the MySQL server using the provided credentials.</li>
<li>It lists all databases, filtering out system databases like 'information_schema' and 'mysql'.</li>
<li>The user is prompted to select a database from the list.</li>
<li>Once a database is selected, the user can run SQL commands (SELECT, INSERT, UPDATE, DELETE, etc.) directly on the database.</li>
<li>The results of SELECT or DESCRIBE queries are displayed in a table format.</li>
<li>The user can exit the command interface by typing exit.</li>

</ol>



## Example Interaction
``` bash
$ python mysql_cli.py 127.0.0.1 root password
Successfully connected to MySQL server
Available Databases:
1. database1
2. database2
3. database3

Enter the number of the database you want to use: 1
Using database: database1

Enter your SQL command (or type 'exit' to quit): SELECT * FROM users;
+----+-------+-------------------+
| ID | Name  | Email             |
+----+-------+-------------------+
| 1  | John  | john@example.com   |
| 2  | Jane  | jane@example.com   |
+----+-------+-------------------+

Enter your SQL command (or type 'exit' to quit): exit
Exiting the SQL interface...

```
## Notes
<ol>
<li>Ensure your MySQL server is running and accessible, and that the user credentials provided have the necessary privileges to list databases and run SQL commands.</li>
<li>If you encounter any issues, please check the MySQL server connection and ensure the necessary ports are open.</li>  
</ol>


## License
This script is released under the MIT License.

## Contact
If you have any questions or suggestions, feel free to open an issue or contact me at the email in my bio.


