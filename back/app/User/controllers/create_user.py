# app/User/controllers/create_user.py

from fastapi import APIRouter
 # 确保这里的导入路径是正确的
from ..models import User
router = APIRouter()

@router.post("/create-user")
async def create_user(user: User):
    # 创建用户的逻辑
    print('123')