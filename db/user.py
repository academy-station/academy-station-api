from db import *


def db_add_user(user):
    res = db["user"].update_one({"_id": user['wxid']}, {"$set": user}, upsert=True)
    print(res.raw_result)

