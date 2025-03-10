from fastapi import FastAPI
from database import engine, Base
from routes import auth, users



app = FastAPI()

app.include_router(auth.router, prefix="/auth")
app.include_router(users.router, prefix="/users")
