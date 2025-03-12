import configparser
from neo4j import GraphDatabase
import pandas as pd
import os

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read("config.ini")

# Read Neo4j credentials
NEO4J_URI = config["NEO4J"]["NEO4J_URI"]
NEO4J_USER = config["NEO4J"]["NEO4J_USER"]
NEO4J_PASSWORD = config["NEO4J"]["NEO4J_PASSWORD"]

# Connect to Neo4j
class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def run_query(self, query, parameters=None):
        with self.driver.session() as session:
            return session.run(query, parameters)

# Initialize Neo4j connection
neo4j_conn = Neo4jConnection(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD)

# Function to delete all nodes and relationships
def clear_database():
    print("⚠️ Deleting all nodes and relationships from Neo4j...")
    neo4j_conn.run_query("MATCH (n) DETACH DELETE n;")
    print("✅ Database cleared!")

# Ensure all CSV files exist
data_files = ["persons.csv", "contacts.csv", "orders.csv", "events.csv"]
for file in data_files:
    if not os.path.exists(file):
        print(f"❌ Error: {file} not found. Ensure it's in the same directory as this script.")
        exit()

# Load CSV data
persons_df = pd.read_csv("persons.csv")
contacts_df = pd.read_csv("contacts.csv")
orders_df = pd.read_csv("orders.csv")
events_df = pd.read_csv("events.csv")

# Function to create nodes
def create_nodes():
    print("🚀 Creating nodes...")

    # Create Person nodes
    for _, row in persons_df.iterrows():
        query = """
        MERGE (p:Person {id: $id, firstName: $firstName, lastName: $lastName, fullName: $fullName, city: $city})
        """
        parameters = {
            "id": row["personId"], 
            "firstName": row["firstName"], 
            "lastName": row["lastName"], 
            "fullName": row["fullName"], 
            "city": row["city"]
        }
        neo4j_conn.run_query(query, parameters)

    # Create Contact nodes
    for _, row in contacts_df.iterrows():
        query = """
        MERGE (c:Contact {id: $id, email: $email})
        """
        parameters = {"id": row["contactId"], "email": row["email"]}
        neo4j_conn.run_query(query, parameters)

    # Create Event nodes
    for _, row in events_df.iterrows():
        query = """
        MERGE (e:Event {id: $id, name: $name, category: $category, city: $city, startDate: $startDate})
        """
        parameters = {"id": row["eventId"], "name": row["eventName"], "category": row["category"], "city": row["city"], "startDate": row["startDate"]}
        neo4j_conn.run_query(query, parameters)

    # Create Order nodes
    for _, row in orders_df.iterrows():
        query = """
        MERGE (o:Order {id: $id})
        """
        parameters = {"id": row["orderId"]}
        neo4j_conn.run_query(query, parameters)

    print("✅ Nodes created successfully!")

# Function to create relationships
def create_relationships():
    print("🔗 Creating relationships...")

    # Link Person to Contact
    for _, row in contacts_df.iterrows():
        query = """
        MATCH (p:Person {id: $person_id})
        MATCH (c:Contact {id: $contact_id})
        MERGE (p)-[:HAS_CONTACT]->(c)
        """
        parameters = {"person_id": row["personId"], "contact_id": row["contactId"]}
        neo4j_conn.run_query(query, parameters)

    # Link Contact to Order
    for _, row in orders_df.iterrows():
        query = """
        MATCH (c:Contact {id: $contact_id})
        MATCH (o:Order {id: $order_id})
        MERGE (c)-[:PLACED_ORDER]->(o)
        """
        parameters = {"contact_id": row["contactId"], "order_id": row["orderId"]}
        neo4j_conn.run_query(query, parameters)

    # Link Order to Event
    for _, row in orders_df.iterrows():
        query = """
        MATCH (o:Order {id: $order_id})
        MATCH (e:Event {id: $event_id})
        MERGE (o)-[:INCLUDES]->(e)
        """
        parameters = {"order_id": row["orderId"], "event_id": row["eventId"]}
        neo4j_conn.run_query(query, parameters)

    print("✅ Relationships created successfully!")

# Run the functions
clear_database()  # Deletes all existing data before inserting new records
create_nodes()  # Creates fresh nodes
create_relationships()  # Creates relationships

# Close Neo4j connection
neo4j_conn.close()

print("🎉 Neo4j data import completed successfully!")
