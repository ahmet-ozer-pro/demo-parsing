import psycopg2
import csv

# Database connection parameters
db_params = {
    "host": "localhost",
    "database": "postgres",
    "user": "postgres",
    "password": "123",
}

# CSV file path
csv_file_path = "/Users/ahmetozer/Desktop/demo-parsing/output/parsed_serverlogs.csv"

def create_table_if_not_exists(conn):
    cur = conn.cursor()
    # Define your table schema here
    table_schema = """
        CREATE TABLE IF NOT EXISTS serverlogs (
            id SERIAL PRIMARY KEY,
            ip_address TEXT,
            timestamp_ TIMESTAMP WITHOUT TIME ZONE,
            request_method TEXT,
            url TEXT,
            response_code TEXT,
            user_agent TEXT,
            request_successful TEXT,
            request_failed TEXT
        )
    """
    cur.execute(table_schema)
    conn.commit()

def insert_data_from_csv(conn, csv_path):
    cur = conn.cursor()
    with open(csv_path, 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        next(csv_reader)  # Skip header row if it exists
        for row in csv_reader:
            # Modify this INSERT statement based on your CSV structure
            insert_query = """
                INSERT INTO serverlogs (ip_address, timestamp_, request_method, url, response_code, user_agent, request_successful, request_failed)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
            """
            cur.execute(insert_query, (
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7]
            ))
    conn.commit()

def main():
    connection = None  # Initialize the connection variable outside the try block
    try:
        connection = psycopg2.connect(**db_params)
        create_table_if_not_exists(connection)
        insert_data_from_csv(connection, csv_file_path)
        print("Data inserted successfully.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        if connection:
            connection.close()

if __name__ == "__main__":
    main()
