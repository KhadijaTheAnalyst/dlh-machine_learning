#!/usr/bin/env python3
""" 105-students """


def top_students(mongo_collection):
    """Returns all students sorted by average score"""

    pipeline = [
        {
            "$group": {
                "_id": "$name",
                "averageScore": {"$avg": "$score"}
            }
        },
        {
            "$sort": {"averageScore": -1}
        },
        {
            # Rename _id to name for output format
            "$project": {
                "name": "$_id",
                "averageScore": 1,
                "_id": 0
            }
        }
    ]
    return list(mongo_collection.aggregate(pipeline))
