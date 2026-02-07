from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import List, Optional
import uvicorn

app = FastAPI(
    title="FastAPI Boilerplate",
    description="A simple FastAPI application with basic CRUD endpoints",
    version="1.0.0"
)

# CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Pydantic models for request/response validation
class UserBase(BaseModel):
    name: str
    email: EmailStr


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        from_attributes = True


# In-memory database (replace with real database in production)
fake_db: List[User] = [
    User(id=1, name="John Doe", email="john@example.com"),
    User(id=2, name="Jane Smith", email="jane@example.com"),
]
next_id = 3


@app.get("/")
async def root():
    """
    Root endpoint with API information
    """
    return {
        "message": "Welcome to FastAPI Boilerplate",
        "version": "1.0.0",
        "docs": "/docs",
        "endpoints": {
            "GET /": "This endpoint",
            "GET /health": "Health check",
            "GET /api/users": "Get all users",
            "GET /api/users/{user_id}": "Get a specific user",
            "POST /api/users": "Create a user",
            "PUT /api/users/{user_id}": "Update a user",
            "DELETE /api/users/{user_id}": "Delete a user"
        }
    }


@app.get("/health")
async def health():
    """
    Health check endpoint
    """
    return {
        "status": "healthy",
        "message": "Service is running"
    }


@app.get("/api/users", response_model=List[User])
async def get_users():
    """
    Get all users
    """
    return fake_db


@app.get("/api/users/{user_id}", response_model=User)
async def get_user(user_id: int):
    """
    Get a specific user by ID
    """
    for user in fake_db:
        if user.id == user_id:
            return user
    raise HTTPException(status_code=404, detail="User not found")


@app.post("/api/users", response_model=User, status_code=201)
async def create_user(user: UserCreate):
    """
    Create a new user
    """
    global next_id
    
    # Check if email already exists
    for existing_user in fake_db:
        if existing_user.email == user.email:
            raise HTTPException(status_code=400, detail="Email already registered")
    
    new_user = User(id=next_id, **user.dict())
    fake_db.append(new_user)
    next_id += 1
    return new_user


@app.put("/api/users/{user_id}", response_model=User)
async def update_user(user_id: int, user: UserCreate):
    """
    Update an existing user
    """
    for idx, existing_user in enumerate(fake_db):
        if existing_user.id == user_id:
            updated_user = User(id=user_id, **user.dict())
            fake_db[idx] = updated_user
            return updated_user
    raise HTTPException(status_code=404, detail="User not found")


@app.delete("/api/users/{user_id}", status_code=204)
async def delete_user(user_id: int):
    """
    Delete a user
    """
    for idx, user in enumerate(fake_db):
        if user.id == user_id:
            fake_db.pop(idx)
            return None
    raise HTTPException(status_code=404, detail="User not found")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
