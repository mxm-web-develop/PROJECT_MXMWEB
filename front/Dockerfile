FROM node:latest as build
WORKDIR /app
COPY ./front/package.json ./front/package-lock.json* ./
RUN npm install -g typescript  # 全局安装 TypeScript
RUN npm install  # 安装所有依赖项
COPY ./front .
RUN npm run build


# 使用 Nginx 镜像作为运行环境
FROM nginx:alpine
COPY --from=build /app/dist /usr/share/nginx/html
# 将 Nginx 配置文件复制到 conf.d 目录
COPY ./front/nginx.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]
