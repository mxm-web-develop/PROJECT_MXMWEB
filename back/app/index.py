from fastapi import FastAPI
from .User.index import user_routers

# from .Product.index import product_routers
app = FastAPI()

# ...数据库和其他配置...

# 将所有模块的路由添加到FastAPI应用中
# all_routers = (user_routers, order_routers, product_routers)
all_routers = (user_routers)
for routers in all_routers:
    for router in routers:
        app.include_router(router)