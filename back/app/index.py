# app/index.py 或 main.py
from fastapi import FastAPI
from .user import user_routers
from .database import connect_to_db,close_db_connection
app = FastAPI()

@app.router.lifecycle.on_startup
async def startup():
    await connect_to_db()

@app.router.lifecycle.on_shutdown
async def shutdown():
    await close_db_connection()

# 将User模块的路由添加到FastAPI应用中
for router in user_routers:
    app.include_router(router)