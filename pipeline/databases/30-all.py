#!/usr/bin/env python3
"""
<<<<<<< HEAD
Defines function that lists all documents in MongoDB collection
=======
List all documents
>>>>>>> d01a612edafbcb20b156d4f8e219d7deae1f7d56
"""


def list_all(mongo_collection):
<<<<<<< HEAD
    """
    Lists all documents in given MongoDB collection

    parameters:
        mongo_collection: the collection to use

    returns:
        list of all documents or 0 if no documents found
    """
    all_docs = []
    collection = mongo_collection.find()
    for document in collection:
        all_docs.append(document)
    return all_docs
=======
    """ Return a list of all documents

    Args:
        mongo_collection (mongocollection): Mongo collection

    Returns:
        _type_: _description_
    """
    all_documents = mongo_collection.find()
    documents_list = list(all_documents)

    return documents_list
>>>>>>> d01a612edafbcb20b156d4f8e219d7deae1f7d56
