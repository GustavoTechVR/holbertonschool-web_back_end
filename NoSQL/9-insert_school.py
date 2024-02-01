#!/usr/bin/env python3
""" 9-insert_school """
from pymongo.collection import Collection
from typing import Any


def insert_school(mongo_collection: Collection, **kwargs: Any) -> Any:
    """
    Inserts a new document into a MongoDB collection based on kwargs.

    Args:
        mongo_collection: The pymongo collection object.
        kwargs: Keyword arguments representing the attributes of the new document.

    Returns:
        The new _id of the inserted document.
    """
    new_document = kwargs
    result = mongo_collection.insert_one(new_document)
    return result.inserted_id
