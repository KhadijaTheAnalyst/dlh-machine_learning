#!/usr/bin/env python3
"""
Analyze Nginx logs from MongoDB with top 10 IPs

This module provides statistics about Nginx logs stored in MongoDB.
It connects to the 'logs' database and 'nginx' collection to analyze:
- Total number of logs
- Count of logs by HTTP method (GET, POST, PUT, PATCH, DELETE)
- Count of GET requests to the /status endpoint
- Top 10 most common IP addresses
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
       - Top 10 most common IP addresses
    
    Output format:
        x logs
        Methods:
            method GET: y
            method POST: z
            method PUT: a
            method PATCH: b
            method DELETE: c
        GET /status: d
        IPs:
            IP1: count1
            IP2: count2
            ... (top 10)
    """

    # ============================================================
    # Connect to MongoDB
    # ============================================================
    client = MongoClient('mongodb://localhost:27017/')
    db = client['logs']
    collection = db['nginx']

    # ============================================================
    # Total logs count
    # ============================================================
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")

    # ============================================================
    # Count by HTTP method
    # ============================================================
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # ============================================================
    # Count GET /status requests
    # ============================================================
    status_count = collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_count} status check")

    # ============================================================
    # TOP 10 IP ADDRESSES (NEW SECTION)
    # ============================================================
    print("IPs:")

    # Define aggregation pipeline for IP analysis
    ip_pipeline = [
        {
            # Group by IP address and count occurrences
            "$group": {
                "_id": "$ip",           # Group by IP field
                "count": {"$sum": 1}    # Count documents in each group
            }
        },
        {
            # Sort by count descending (highest first)
            "$sort": {"count": -1}
        },
        {
            # Get only top 10
            "$limit": 10
        }
    ]

    # Run the aggregation pipeline
    top_ips = collection.aggregate(ip_pipeline)

    # Print each IP with its count
    for ip_doc in top_ips:
        ip_address = ip_doc["_id"]      # The IP address (from _id field)
        ip_count = ip_doc["count"]      # The count of occurrences
        print(f"\t{ip_address}: {ip_count}")

    # ============================================================
    # Close connection
    # ============================================================
    client.close()


if __name__ == "__main__":
    log_stats()
