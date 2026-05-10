#!/usr/bin/env python3
"""Update school topics in a MongoDB collection"""


def update_topics(mongo_collection, name, topics):
    """
    Updates the topics for a school document.

    Args:
        mongo_collection: A pymongo collection object
        name: The school name to find (string)
        topics: List of topics to set (list of strings)

    Returns:
        The update result object
    """
    result = mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
    return result
