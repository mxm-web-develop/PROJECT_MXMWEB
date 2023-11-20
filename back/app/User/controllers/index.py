from .create_user import router as create_user_router
from .get_user import router as get_user_router

# 你可以选择导出单独的路由或者合并它们
routers = (create_user_router, get_user_router)