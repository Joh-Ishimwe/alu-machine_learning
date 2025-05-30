#!/usr/bin/env python3
"""
<<<<<<< HEAD
Provides some stats about Nginx logs stored in MongoDB
=======
Nginx logs stored in MongoDB:
>>>>>>> d01a612edafbcb20b156d4f8e219d7deae1f7d56
"""


from pymongo import MongoClient


<<<<<<< HEAD
if __name__ == "__main__":
    """
    Gets stats about Nginx logs stored in MongoDB
    """
    client = MongoClient('mongodb://127.0.0.1:27017')
    logs_coll = client.logs.nginx
    doc_count = logs_coll.count_documents({})
    print("{} logs".format(doc_count))
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = logs_coll.count_documents({"method": method})
        print("\tmethod {}: {}".format(method, method_count))
    filter_path = {"method": "GET", "path": "/status"}
    path_count = logs_coll.count_documents(filter_path)
    print("{} status check".format(path_count))
=======
if __name__ == '__main__':

    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    # Get the total number of documents
    total_logs = collection.count_documents({})

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents(
        {"method": method}) for method in methods}

    # Get the count of status check
    status_check_count = collection.count_documents(
        {"method": "GET", "path": "/status"})

    # Print the stats
    print(f"{total_logs} logs")
    print("Methods:")
    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")
    print(f"{status_check_count} status check")
>>>>>>> d01a612edafbcb20b156d4f8e219d7deae1f7d56
