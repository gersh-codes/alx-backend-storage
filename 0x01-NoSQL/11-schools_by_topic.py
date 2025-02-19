#!/usr/bin/env python3
""" MongoDB operations in Python using pymongo """

def schools_by_topic(mongo_collection, topic):
    """returns the list of school having a specific topic"""
    topic_filter = {
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    }
    return [doc for doc in mongo_collection.find(topic_filter)]
