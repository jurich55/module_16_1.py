from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/user/admin")
async def get_admin(admin: str = 'Fedor'):
    return {"message": f"Имя: {admin}, Вы вошли как администратор"}

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    return {"message": f"Вы вошли как пользователь № {user_id}"}

@app.put("/user")
async def put_user(username: str = 'Bob', age: int = 25) -> dict:
    return {"message": f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

@app.get("/")
async def in_put():
    return {"message": "Главная страница"}

#  uvicorn main:app --reload

#  http://127.0.0.1:8000/docs
#  http://127.0.0.1:8000/redoc
