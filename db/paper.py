from db import *


def db_upload_paper(paper):
    res = db["paper"].update_one({"_id": paper["id"]}, {"$set": paper}, upsert=True)
    return res.raw_result


def db_submit_paper(id):
    res = db["paper"].update_one({"_id": id}, {"$set": {"status": "pending"}}, upsert=False)
    return res.raw_result


def db_query_papers(user_openid: str):
    res = db["paper"].find({"user_openid": user_openid})
    return list(res)
