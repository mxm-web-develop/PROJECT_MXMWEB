# app/User/controllers/get_user.py

from fastapi import APIRouter
 # 确保这里的导入路径是正确的
from ..models import User
router = APIRouter()

@router.get("/get-user")
async def get_user():
    # 创建用户的逻辑
    print('123')
    return '123123123'