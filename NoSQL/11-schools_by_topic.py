#!/usr/bin/env python3
"""Schools by topics"""

import pymongo


def schools_by_topic(mongo_collection, topic):
    return [school for school in mongo_collection.find({"topics": topic})]
