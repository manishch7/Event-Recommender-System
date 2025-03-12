import pandas as pd
import numpy as np

# Seed for reproducibility
np.random.seed(42)

# Extended lists for diverse names and cities
first_names = [
    "Emma", "Olivia", "Ava", "Sophia", "Isabella", "Mia", "Charlotte",
    "Amelia", "Harper", "Evelyn", "Liam", "Noah", "Oliver", "Elijah",
    "James", "William", "Benjamin", "Lucas", "Henry", "Alexander"
]
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller",
    "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez",
    "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin"
]
cities = [
    "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia",
    "San Antonio", "San Diego", "Dallas", "San Jose", "Austin", "Seattle",
    "Denver", "Miami", "Boston", "Las Vegas", "Atlanta", "Portland"
]

# 1️⃣ Create persons.csv (1000 records)
persons = pd.DataFrame({
    'personId': [f'P{i}' for i in range(1, 1001)],
    'firstName': np.random.choice(first_names, 1000),
    'lastName': np.random.choice(last_names, 1000),
    'city': np.random.choice(cities, 1000),
})
persons["fullName"] = persons["firstName"] + " " + persons["lastName"]
persons.to_csv('persons.csv', index=False)
print("✅ persons.csv created with 1000 records!")

# 2️⃣ Create events.csv (500 records)
event_adjectives = ["Annual", "International", "Grand", "Modern", "Cultural", "Dynamic", "Spectacular"]
event_nouns = ["Music Festival", "Art Expo", "Tech Summit", "Food Carnival", "Literary Fair", "Comedy Show", "Startup Pitch"]
categories = ['Sport', 'Music', 'Comedy', 'Literature', 'Food', 'Conference', 'Art', 'Technology', 'Film', 'Fashion']

events = pd.DataFrame({
    'eventId': [f'E{i}' for i in range(1, 501)],
    'eventName': [f"{np.random.choice(event_adjectives)} {np.random.choice(event_nouns)}" for _ in range(500)],
    'startDate': pd.date_range(start='2024-01-01', periods=500, freq='D'),
    'category': np.random.choice(categories, 500),
    'city': np.random.choice(cities, 500),
})
events.to_csv('events.csv', index=False)
print("✅ events.csv created with 500 records!")

# 3️⃣ Create contacts.csv (1500 records)
selected_persons = np.random.choice(persons['personId'], 1500, replace=True)
emails = []
for i in range(1500):
    person = persons[persons['personId'] == selected_persons[i]].iloc[0]
    email = f"{person['firstName'].lower()}.{person['lastName'].lower()}{np.random.randint(1,1000)}@example.com"
    emails.append(email)

contacts = pd.DataFrame({
    'contactId': [f'C{i}' for i in range(1, 1501)],
    'personId': selected_persons,
    'email': emails,
})
contacts.to_csv('contacts.csv', index=False)
print("✅ contacts.csv created with 1500 records!")

# 4️⃣ Create orders.csv (2000 records)
orders = pd.DataFrame({
    'orderId': [f'O{i}' for i in range(1, 2001)],
    'contactId': np.random.choice(contacts['contactId'], 2000),
    'eventId': np.random.choice(events['eventId'], 2000),
})
orders.to_csv('orders.csv', index=False)
print("✅ orders.csv created with 2000 records!")

print("🎉 All CSV files created successfully!")
