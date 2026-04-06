from fastapi import FastAPI
from app.database import Base, engine

from app.routes import user_routes, record_routes, dashboard_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(prefix ="/api" , tags = ["Finance Dashboard API"])

app.include_router(user_routes.router)
app.include_router(record_routes.router)
app.include_router(dashboard_routes.router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Finance Dashboard API!"}