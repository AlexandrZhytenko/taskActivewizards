
import zipfile
import pymongo
from pymongo import MongoClient
from bson.json_util import loads

def upload_file_into_db(input_zip, name_db="world_bank", collection_name="world"):
    client = MongoClient('localhost', 27017)
    print "Connected successfully"
    db = client[name_db]
    collection = db[collection_name]
    data_info = db.data_info
    with zipfile.ZipFile(input_zip, "r") as myzip:
        for filename in myzip.namelist():
            with myzip.open(filename) as open_file:
                for row in open_file:
                    line = loads(row)
                    print line
                    data_info.insert_one(line)
    print data_info

    import pprint
    for i in data_info.find():
        pprint.pprint(i)
    print data_info.count()

if __name__ == "__main__":
    input_zip = "world_bank.zip"
    upload_file_into_db(input_zip)