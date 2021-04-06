from fastapi import FastAPI
from api.root import api_root

app = FastAPI(title="Academy Studio API")
app.include_router(api_root)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=2021, reload=True,
                ssl_keyfile="/etc/ssl/2_nanchuan.site.key",
                ssl_certfile="/etc/ssl/1_nanchuan.site_bundle.crt")

