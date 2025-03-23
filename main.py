import mysql.connector
from mysql.connector import Error
import argparse

def connect_to_mysql_server(host, user, password):
    """Establish connection to MySQL server."""
    try:
        connection = mysql.connector.connect(
            host=host,  # MySQL host (IP or URL)
            user=user,  # MySQL username
            password=password  # MySQL password
        )
        if connection.is_connected():
            print("Successfully connected to MySQL server")
            return connection
    except Error as e:
        print(f"Error: {e}")
        return None

def list_databases(connection):
    """List all user databases, filtering out system databases."""
    try:
        cursor = connection.cursor()
        cursor.execute("SHOW DATABASES")
        databases = cursor.fetchall()
        print("\nAvailable Databases:")
        filtered_databases = [db[0] for db in databases if db[0] not in ('information_schema', 'performance_schema', 'mysql', 'sys')]
        
        if filtered_databases:
            for idx, db in enumerate(filtered_databases, 1):
                print(f"{idx}. {db}")
        else:
            print("No databases available.")
        
        cursor.close()
        return filtered_databases
    except Error as e:
        print(f"Error listing databases: {e}")
        return []

def select_database(connection, databases):
    """Let the user choose a database from the filtered list."""
    while True:
        db_choice = input("Enter the number of the database you want to use: ")
        try:
            db_choice = int(db_choice)
            if 1 <= db_choice <= len(databases):
                chosen_db = databases[db_choice - 1]
                connection.database = chosen_db
                print(f"Using database: {chosen_db}")
                return chosen_db
            else:
                print("Invalid choice. Please select a valid number.")
        except ValueError:
            print("Please enter a valid number.")

def format_table_output(columns, results):
    """Format and display the results of a SELECT or DESCRIBE query in a table-like format."""
    # Create the header row
    header = " | ".join([col for col in columns])
    separator = "+".join(["-" * len(col) for col in columns])
    
    # Print the header
    print("\n+" + separator + "+")
    print(f"| {header} |")
    print("+" + separator + "+")
    
    # Print each result row
    for row in results:
        row_display = " | ".join([str(value) if value is not None else "NULL" for value in row])
        print(f"| {row_display} |")
    
    # Print the bottom separator
    print("+" + separator + "+")

def execute_command(connection):
    """Execute SQL command entered by the user."""
    cursor = connection.cursor()
    
    while True:
        # Get the SQL command from the user
        command = input("Enter your SQL command (or type 'exit' to quit): ")
        
        if command.lower() == 'exit':
            print("Exiting the SQL interface...")
            break
        
        try:
            # Execute the SQL command
            cursor.execute(command)
            # Commit if it's a modifying query (e.g., INSERT, UPDATE, DELETE)
            if command.strip().lower().startswith(('insert', 'update', 'delete')):
                connection.commit()
                print("Command executed successfully")
            else:
                # For SELECT or DESCRIBE queries, fetch and display the result
                results = cursor.fetchall()
                columns = [desc[0] for desc in cursor.description]  # Get column names

                if command.strip().lower().startswith('describe'):
                    # If it's a DESCRIBE query, format it appropriately
                    format_table_output(columns, results)
                elif results:
                    # For SELECT queries, format it as a table
                    format_table_output(columns, results)
                else:
                    print("No results found.")
        except Error as e:
            print(f"Error executing command: {e}")
    
    cursor.close()

def main():
    # Parse command-line arguments for database connection details
    parser = argparse.ArgumentParser(description='Connect to a MySQL database and run commands.')
    parser.add_argument('host', type=str, help='The MySQL server host (IP address or domain name)')
    parser.add_argument('user', type=str, help='The MySQL username')
    parser.add_argument('password', type=str, help='The MySQL password')
    
    args = parser.parse_args()

    # Connect to the MySQL server using provided arguments
    connection = connect_to_mysql_server(args.host, args.user, args.password)
    
    if connection:
        # List databases and let the user choose one
        databases = list_databases(connection)
        
        if not databases:
            print("No databases available to choose from. Exiting.")
            return
        
        # Let the user choose a database
        select_database(connection, databases)
        
        # Allow the user to execute commands on the selected database
        execute_command(connection)
        
        # Close the connection after use
        connection.close()

if __name__ == "__main__":
    main()
