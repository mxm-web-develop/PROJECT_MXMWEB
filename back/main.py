import os
import uvicorn

host = os.getenv("HOST", "127.0.0.1")
port = int(os.getenv("PORT", 8000))

if __name__ == "__main__":
    uvicorn.run("app.index:app", host=host, port=port)
