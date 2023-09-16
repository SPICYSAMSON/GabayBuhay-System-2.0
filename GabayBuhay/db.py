from sqlalchemy import create_engine, text
from pprint import pprint
import os

# Create a database engine
DB_CONNECTION_STRING = "mysql+pymysql://root:HAKDUGERZ69@127.0.0.1:3306/gabaybuhay?charset=utf8mb4"

engine = create_engine(DB_CONNECTION_STRING)


def load_roles_from_db():
    '''Gets the role_id and role_name from the gabaybuhay.roles table.'''
    try:
        # Connect to the database
        with engine.connect() as conn:
            # Execute a SQL query to select all records from the "roles" table
            result = conn.execute(text("SELECT * FROM roles"))
            # Fetch and convert the query results to a list of dictionaries
            roles = [row._asdict() for row in result]
            
            return roles
            
    except Exception as e:
        # Handle any exceptions that may occur during the databaseq interaction
        print("An error occurred:", e)
        

def register_user(user_data):
    ''' Registers the user into the gabaybuhay.users table,
    gets their user_id and role chosen;
    puts it into the gabaybuhay.user_roles table.
    
    
    Determines whether they are a patient or clinician and puts their user_id into the role table (gabaybuhay.patient / gabaybuhay.clinician) where they respectively belong.'''
    
    
    try:
        with engine.connect() as conn:
            query = text(
                "INSERT INTO users (email, password, first_name, last_name)"
                "VALUES (:email, :password, :first_name, :last_name)"
            )
        
            conn.execute(
                query,
                {
                    'email': user_data['email'],
                    'password': user_data['password'],
                    'first_name': user_data['first_name'],
                    'last_name': user_data['last_name'],
                }
            )
            conn.commit()
            
            query_two = text( 
                "SELECT user_id AS user_id FROM users ORDER BY user_id DESC LIMIT 1"
            )
            
            result = conn.execute(query_two)
            row = result.fetchone()  # Fetch the first (and only) row
            if row:
                user_id = row[0] # Get the user_id value from the row, dito yung error na 'Error inserting data: tuple indices must be integers or slices, not str' kasi naka row['user_id'] ka kanina (Sep 12, 2023 around 7:45pm). 
            else:
                user_id = None  # Handle the case where no user is found

            # Check if you have a valid user_id and account_type
            if user_id is not None and 'account_type' in user_data:
                role_id =  user_data['account_type'][0]

                query_three = text(
                    "INSERT INTO user_roles (user_id, role_id) "
                    "VALUES (:user_id, :role_id)"
                )

                # Execute the second query to insert user role data
                conn.execute(
                    query_three,
                    {
                        'user_id': user_id,
                        'role_id': role_id,
                    }
                )

            # Commit the transaction to save changes to the database
            conn.commit()
            
            role_id_int = int(role_id)
            if role_id_int == 1:
                insert_to_patient(user_data, user_id, conn)
            elif role_id_int == 2:
                insert_to_clinician(user_data, user_id, conn)

    except Exception as e:
        # Log any exceptions that occur
        print(f"Error inserting data: {str(e)}")
        
        
def insert_to_patient(patient_data, user_id, conn):
    query = text(
        "INSERT INTO patient (user_id)"
        "VALUES (:user_id)"
    )
    
    conn.execute(
            query,
                {
                    'user_id': user_id
                }
            )
    conn.commit()

def insert_to_clinician(clinician_data, user_id, conn):
    query = text(
        "INSERT INTO clinician (user_id, license)"
        "VALUES (:user_id, :license)"
    )
    
    conn.execute(
            query,
                {
                    'user_id': user_id,
                    'license': clinician_data['clinician_license']
                }
            )
    conn.commit()


            
            