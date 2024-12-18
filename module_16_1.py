from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
async def in_put()->str:
    return "Главная страница"

@app.get("/user/admin")
async def get_admin(admin: str = 'Fedor')->str:
    return f"Имя: {admin}, Вы вошли как администратор"

@app.get("/user/{user_id}")
async def get_user(user_id: int) ->str:
    return f"Вы вошли как пользователь № {user_id}"

@app.put("/user")
async def put_user(username: str = 'Bob', age: int = 25) ->str:
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"



#  uvicorn module_16_1:app --reload

#  http://127.0.0.1:8000/docs
#  http://127.0.0.1:8000/redoc

