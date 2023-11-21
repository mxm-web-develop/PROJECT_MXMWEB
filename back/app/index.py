# app/index.py 或 main.py
from fastapi import FastAPI
from .User import user_routers

app = FastAPI()

# 将User模块的路由添加到FastAPI应用中
for router in user_routers:
    app.include_router(router)