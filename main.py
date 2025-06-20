from typing import Optional
from fastapi import FastAPI
from fastapi.responses import HTMLResponse  # インポート
import random  # randomライブラリを追加

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Optional[str] = None):
    return {"item_id": item_id, "q": q}

@app.get("/omikuji")
def omikuji():
    omikuji_list = [
        "大吉", "中吉", "小吉", "吉", "半吉", "末吉", "末小吉", "凶", "小凶", "大凶"
    ]
    return omikuji_list[random.randrange(10)]

@app.get("/index")
def index():
    html_content = """
    <html>
        <head>
            <title>programing is hard</title>
        </head>
        <body>
            <h1>プログラミング大変だ！</h1>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content, status_code=200)

@app.post("/present")
async def give_present(present: str):  # 型指定（任意）を追加
    return {"response": f"サーバです。メリークリスマス！ {present}ありがとう。お返しはキャンディーです。"}
