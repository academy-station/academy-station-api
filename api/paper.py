import json
import os
from pprint import pprint

from fastapi import File, UploadFile, APIRouter, Form
from fastapi.responses import FileResponse

from db.paper import db_upload_paper, db_query_papers, db_submit_paper
from settings import DATA_DIR

api_paper = APIRouter(tags=["paper"])


def get_file_path(id: str):
    return os.path.join(DATA_DIR, id)


def download_file(file: UploadFile, file_path: str):
    f1 = file.file.read()
    with open(file_path, "wb") as f2:
        f2.write(f1)


@api_paper.post("/upload/", summary="上传论文")
async def create_upload_paper(
        file: UploadFile = File(...),
        data: str = Form(...)
):
    upload_temp_file_data = json.loads(data)
    user_openid = upload_temp_file_data["user_openid"]
    file_data = upload_temp_file_data["file"]
    name = file_data["name"]
    time = file_data["time"]
    path = file_data["path"]
    size = file_data["size"]
    id = f"{time}-{name}"

    # 下载文件
    download_file(file, get_file_path(id))

    # 返回数据
    data = {
        "id": id,
        "user_openid": user_openid,
        "file_name": name,
        "file_size": size,
        "file_path": path,
        "time": time,
        "status": "uploaded",
    }
    db_upload_paper(data)
    pprint(data)
    return data


@api_paper.get("/submit/")
async def submit_paper(id: str):
    res = db_submit_paper(id)
    return res


@api_paper.get("/query/", summary="获取论文列表")
async def query_papers(user_openid: str = "test"):
    return db_query_papers(user_openid)


@api_paper.get("/download/", summary="下载报告")
async def download_paper(id: str = "test.json"):
    return FileResponse(get_file_path(id))
