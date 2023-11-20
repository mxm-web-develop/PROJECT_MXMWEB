FROM python:3.9

# 设置工作目录
WORKDIR /usr/src/app

# 复制 requirements.txt 并安装依赖
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用代码
COPY ./app /usr/src/app/app
COPY main.py /usr/src/app/

# 暴露端口
EXPOSE 8000

# 运行应用
CMD ["python", "main.py"]
