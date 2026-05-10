#!/usr/bin/env python3
"""
Analyze Nginx logs from MongoDB

This module provides statistics about Nginx logs stored in MongoDB.
It connects to the 'logs' database and 'nginx' collection to analyze:
- Total number of logs
- Count of logs by HTTP method (GET, POST, PUT, PATCH, DELETE)
- Count of GET requests to the /status endpoint
"""


from pymongo import MongoClient


def log_stats():
    """
    Print statistics about Nginx logs stored in MongoDB.
    
    This function:
    1. Connects to MongoDB on localhost:27017
    2. Accesses the 'logs' database and 'nginx' collection
    3. Calculates and displays:
       - Total number of log documents
       - Count of each HTTP method
       - Count of GET requests to /status path
    
    Output format:
        x logs
        Methods:
            GET: y
            POST: z
            PUT: a
            PATCH: b
            DELETE: c
        GET /status: d
    """

    # ============================================================
    # STEP 1: Connect to MongoDB
    # ============================================================
    # Create a MongoDB client connection to localhost on port 27017
    # This is the default MongoDB connection string
    client = MongoClient('mongodb://localhost:27017/')

    # ============================================================
    # STEP 2: Access the Database and Collection
    # ============================================================
    # Access the 'logs' database
    # (MongoDB creates it if it doesn't exist)
    db = client['logs']

    # Access the 'nginx' collection within the 'logs' database
    # (A collection is like a table in relational databases)
    collection = db['nginx']

    # ============================================================
    # STEP 3: Count Total Number of Logs
    # ============================================================
    # count_documents({}) counts ALL documents in the collection
    # An empty filter {} means no restrictions
    # This gives us the total number of Nginx log entries
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # ============================================================
    # STEP 4: Define HTTP Methods to Analyze
    # ============================================================
    # List of HTTP methods we want to count
    # Must be in this exact order: GET, POST, PUT, PATCH, DELETE
    # as specified in the task requirements
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    # ============================================================
    # STEP 5: Display Methods Section Header
    # ============================================================
    # Print the "Methods:" header before listing counts
    print("Methods:")

    # ============================================================
    # STEP 6: Count Logs for Each HTTP Method
    # ============================================================
    # Loop through each method and count how many logs have that method
    for method in methods:
        # Filter documents where the 'method' field equals the current method
        # count_documents({"method": method}) counts matching documents
        count = collection.count_documents({"method": method})

        # Print with tab character (\t) for proper indentation
        # Format: \t[METHOD]: [COUNT]
        # Example: \tGET: 1234
        print(f"\tmethod {method}: {count}")

    # ============================================================
    # STEP 7: Count GET Requests to /status Endpoint
    # ============================================================
    # This is a special query with TWO conditions:
    # 1. method field must equal "GET"
    # 2. path field must equal "/status"
    # Both conditions must be true (AND operation)
    # This counts requests like: GET /status HTTP/1.1
    status_count = collection.count_documents({"method": "GET", "path": "/status"})

    # Print the count of GET /status requests
    # No tab indentation for this line, as per requirements
    print(f"{status_count} status check")

    # ============================================================
    # STEP 8: Close MongoDB Connection
    # ============================================================
    # Close the connection to free up resources
    # Best practice: always close connections when done
    client.close()


# ============================================================
# MAIN EXECUTION
# ============================================================
# This block only runs if the script is executed directly
# (not if it's imported as a module)
# This is a Python best practice
if __name__ == "__main__":
    # Call the log_stats function to display statistics
    log_stats()
