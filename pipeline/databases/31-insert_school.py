#!/usr/bin/env python3
"""Insert a document in a MongoDB collection"""


def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.

    Args:
        mongo_collection: A pymongo collection object
        **kwargs: Variable keyword arguments forming the document

    Returns:
        The _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
