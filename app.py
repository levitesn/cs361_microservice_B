from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

users = {"admin": "admin"}


class User(BaseModel):
    username: str
    password: str


def create_user(username: str, password: str):
    users[username] = password


def login(username: str, password: str):
    if username in users:
        if users[username] == password:
            return 2
        return 1
    return 0


@app.post("/create_user")
async def create_user_endpoint(user: User):
    if user.username in users:
        raise HTTPException(status_code=400, detail="User already exists")
    create_user(user.username, user.password)
    return {"message": "User created successfully"}


@app.post("/login")
async def login_endpoint(user: User):
    result = login(user.username, user.password)
    if result == 2:
        return {"message": "Login successful"}
    elif result == 1:
        raise HTTPException(status_code=400, detail="Incorrect password")
    else:
        raise HTTPException(status_code=404, detail="User not found")


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
