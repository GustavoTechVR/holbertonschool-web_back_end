#!/usr/bin/env python3
""" 11-schools_by_topic """
from pymongo.collection import Collection
from typing import List


def schools_by_topic(mongo_collection: Collection, topic: str) -> List[dict]:
    """
    Returns the list of schools having a specific topic.

    Args:
        mongo_collection: The pymongo collection object.
        topic: The topic searched.

    Returns:
        A list of dictionaries representing schools having the specified topic.
    """
    query = {"topics": topic}
    return list(mongo_collection.find(query))
