#!/usr/bin/env python3
"""Find schools by topic in a MongoDB collection"""


def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: A pymongo collection object
        topic: The topic to search for (string)

    Returns:
        A list of school documents containing the topic
    """
    return list(mongo_collection.find({"topics": topic}))
