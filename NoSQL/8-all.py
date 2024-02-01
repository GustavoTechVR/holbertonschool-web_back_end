#!/usr/bin/env python3
""" 8-all """
from pymongo.collection import Collection
from typing import List


def list_all(mongo_collection: Collection) -> List[dict]:
    """
    Lists all documents in a MongoDB collection.

    Args:
        mongo_collection: The pymongo collection object.

    Returns:
        A list of dictionaries representing the documents in the collection.
    """
    return list(mongo_collection.find({}))
