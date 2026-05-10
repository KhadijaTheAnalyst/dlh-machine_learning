#!/usr/bin/env python3
"""Return top students sorted by average score from MongoDB"""


def top_students(mongo_collection):
    """
    Returns all students sorted by average score (descending).

    Args:
        mongo_collection: A pymongo collection object

    Returns:
        A list of students with averageScore, sorted by score (highest first)
    """
    # Define aggregation pipeline
    pipeline = [
        {
            # Group by name and calculate average score
            "$group": {
                "_id": "$name",
                "averageScore": {"$avg": "$score"}
            }
        },
        {
            # Sort by average score descending (highest first)
            "$sort": {"averageScore": -1}
        }
    ]

    # Run aggregation pipeline and return results as list
    return list(mongo_collection.aggregate(pipeline))
