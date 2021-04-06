import json
import os
from pprint import pprint
from functions.user import getOpenID

from fastapi import File, UploadFile, APIRouter, Form
from settings import DATA_DIR

api_user = APIRouter(tags=["user"])


@api_user.get("/login/", summary="获取OpenID")
def user_login(js_code: str):
    res = getOpenID(js_code)
    return res
