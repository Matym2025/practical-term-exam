from fastapi import FastAPI
from sqlmodel import SQLModel
from typing import Optional, List, Dict, Any

app = FastAPI(title="CRUD usuarios FastAPI (simple)")

# Modelo M.M
class User(SQLModel):
    id: int
    username: str
    password: str
    email: Optional[str] = None
    is_active: bool = True

class UserCreate(SQLModel):
    username: str
    password: str
    email: Optional[str] = None
    is_active: bool = True

# Actualizar M.M
class UserUpdate(SQLModel):
    username: Optional[str] = None
    email: Optional[str] = None
    is_active: Optional[bool] = None

class Credentials(SQLModel):
    username: str
    password: str

# Base datos M.M
users_db: List[User] = []
next_id = 1  


def find_user_by_id(user_id: int) -> Optional[User]:
    for u in users_db:
        if u.id == user_id:
            return u
    return None

def find_user_by_username(username: str) -> Optional[User]:
    for u in users_db:
        if u.username == username:
            return u
    return None

def safe_user(u: User) -> Dict[str, Any]:
    
    return {
        "id": u.id,
        "username": u.username,
        "email": u.email,
        "is_active": u.is_active,
    }


@app.get("/")
def root():
    return {"message": "API de Usuarios - CRUD simple OK"}

# Usuario crear M.M
@app.post("/users")
def create_user(data: UserCreate):
    global next_id
    if find_user_by_username(data.username):
        return {"ok": False, "message": "username ya existe"}

    user = User(
        id=next_id,
        username=data.username,
        password=data.password,
        email=data.email,
        is_active=data.is_active,
    )
    users_db.append(user)
    next_id += 1
    return {"ok": True, "message": "usuario creado", "user": safe_user(user)}

# Listar usuarios M.M
@app.get("/users")
def list_users():
    return {"users": [safe_user(u) for u in users_db]}

# Obtener usuario id M.M
@app.get("/users/{user_id}")
def get_user(user_id: int):
    u = find_user_by_id(user_id)
    if not u:
        return {"ok": False, "message": "no encontrado"}
    return {"ok": True, "user": safe_user(u)}

# Actualizar M.M
@app.put("/users/{user_id}")
def update_user(user_id: int, data: UserUpdate):
    u = find_user_by_id(user_id)
    if not u:
        return {"ok": False, "message": "no encontrado"}

    if data.username and data.username != u.username:
        if find_user_by_username(data.username):
            return {"ok": False, "message": "username ya existe"}
        u.username = data.username

    if data.email is not None:
        u.email = data.email
    if data.is_active is not None:
        u.is_active = data.is_active

    return {"ok": True, "message": "usuario actualizado", "user": safe_user(u)}

# Eliminar M.M
@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    u = find_user_by_id(user_id)
    if not u:
        return {"ok": False, "message": "no encontrado"}
    users_db.remove(u)
    return {"ok": True, "message": "usuario eliminado"}

# Login M.M
@app.post("/login")
def login(creds: Credentials):
    u = find_user_by_username(creds.username)
    if u and u.password == creds.password:
        return {"message": "login successful"}
    return {"message": "Invalid credentials"}