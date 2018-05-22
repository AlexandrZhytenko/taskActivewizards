
import zipfile
import pymongo
from pymongo import MongoClient
from bson.json_util import loads

def upload_file_into_db(input_zip, name_db="world_bank", collection_name="world"):
    try:
        client = MongoClient('localhost', 27017)
        print "Connected successfully."
        db = client[name_db]
        collection = db[collection_name]
        data_info = db.data_info
        with zipfile.ZipFile(input_zip, "r") as myzip:
            for filename in myzip.namelist():
                with myzip.open(filename) as open_file:
                    for row in open_file:
                        line = loads(row)
                        data_info.insert_one(line)
    except pymongo.errors.DuplicateKeyError:
        print "Database has already existed."

if __name__ == "__main__":
    input_zip = "world_bank.zip"
    upload_file_into_db(input_zip)