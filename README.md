# 🎟️ Event Recommender System with Neo4j

## 📖 Project Overview
This project implements an **Event Recommender System** using a **graph database (Neo4j)** to recommend:
- 🔹 **Events for a Contact** (based on similar interests)
- 🔹 **Contacts for an Event** (to target interested attendees)

The recommendation engine uses **Collaborative Filtering** techniques to analyze event participation and suggest relevant recommendations.

## 🚀 Features
✅ **Graph Database Model**: Uses **Neo4j** to store events, contacts, orders, and relationships.  
✅ **Recommender System**: Suggests **best-matching events for a contact** and **best-matching contacts for an event**.  
✅ **Full Data Pipeline**: Generates sample data, loads it into Neo4j, and runs queries.  
✅ **Scalable & Extensible**: Easily extendable for large-scale event data.  

---

## 🛠️ Setup Instructions

### 1️⃣ Install Dependencies
Ensure you have **Python** installed. Then install the required packages:

```bash
pip install neo4j pandas configparser numpy
