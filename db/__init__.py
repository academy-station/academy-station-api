import pymongo
import urllib.parse
from enum import Enum
from typing import Optional
from pydantic import BaseModel

username = urllib.parse.quote_plus("academy_station")
password = urllib.parse.quote_plus("academy_station")
host = "nanchuan.site"
port = 2708

uri = pymongo.MongoClient(f"mongodb://{username}:{password}@{host}:{port}/?"
                          f"authSource=AcademyStation")
db = uri["AcademyStation"]