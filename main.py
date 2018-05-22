from pymongo import MongoClient
from datetime import datetime

def main():
    try:
        c = MongoClient('localhost', 27017)
        print "Connected successfully."
    except pymongo.errors.DuplicateKeyError:
        print "Database has already existed."
    dbh = c["mydb"]
    user_doc = {
        "username": "OlexandrZhytenko",
        "firstname": "Olexandr",
        "surname": "Zhytenko",
        "email": "Zhytenko@ukr.net"
    }
    dbh.users.insert(user_doc)
    # print "successfully inserted {}".format(user_doc)
    # print user_doc

c = MongoClient('localhost', 27017)
print "Connected successfully."
dbh = c["mydb"]
user_doc = dbh.users.find_one({"username": "OlexandrZhytenko"})
if not user_doc:
    print "no document found username OlexandrZhytenko"
else:
    # print user_doc
    pass
users = dbh.users.find({"firstname": "Olexandr"}, {"email":1})
# for user in users:
#     print user.get("email")

# users = dbh.users.find().sort("_id").limit(3)
# print users
# for user in users:
#     print user

user_doc = {
    "username" : "janedoe",
    "firstname" : "Jane",
    "surname" : "Doe",
    "dateofbirth" : datetime(1974, 4, 12),
    "email" : "janedoe74@example.com",
    "score" : 0 }

# import copy
# old_user_doc = dbh.users.find_one({"username":"OlexandrZhytenko"})
# new_user_doc = copy.deepcopy(old_user_doc)
# new_user_doc["email"] = "janedoe74@example2.com"
# dbh.users.update({"username":"OlexandrZhytenko"}, new_user_doc)
# dbh.users.update({"username":"OlexandrZhytenko"}, {"$set":{"email":"janedoe74@example2.com"}})
# dbh.users.remove({"username":"OlexandrZhytenko"})
# print new_user_doc

my_document = {
    "name":"foo document",
    "data":{"name":"bar document"}
}

user_doc = {
    "username":"foouser",
    "twitter":{
        "username":"footwitter",
        "password":"secret",
        "email":"twitter@example.com"
    },
    "facebook":{
        "username":"foofacebook",
        "password":"secret",
        "email":"facebook@example.com"
    },
    "irc":{
        "username":"fooirc",
        "password":"secret",
    }
}


# dbh.users.insert(user_doc)
user_doc = dbh.users.find_one({"facebook.username":"foofacebook"})
print user_doc
# for user in dbh.users.find():
#     print user
# dbh.close()
# # if __name__ == "__main__":
#     main()



