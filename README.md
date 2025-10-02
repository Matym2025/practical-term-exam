# Practical Term Exam

Este repositorio contiene una API REST (FastAPI) para manejo básico de usuarios (CRUD) y autenticación. Incluye un script `brute.sh` pensado para pruebas locales (simula intentos de login).

---

## Contenido del repositorio

- `main.py` — implementación FastAPI con modelos en `sqlmodel` y almacenamiento en memoria (`users_db`).
- `brute.sh` — script bash que prueba múltiples contraseñas contra `http://127.0.0.1:8000/`.
- `requirements.txt` — dependencias: `fastapi`, `uvicorn`, `sqlmodel`.
- `.gitignore` — (recomendado) para evitar subir `venv/`, `__pycache__/`, etc.

---

## Estructura (actual)
```
practical-term-exam/
├── main.py
├── brute.sh
├── requirements.txt
└── (otros archivos opcionales)
```

## Requisitos y preparación

- **Python** 3.10+  
- **pip**

Se recomienda crear un entorno virtual:

**Windows (PowerShell)**
``` bash
python -m venv venv
venv\Scripts\Activate.ps1
```
**Instalar dependencias**
``` bash 
pip install -r requirements.txt
```
**Cómo ejecutar la API**

Desde la raíz del proyecto, con el entorno virtual activado:
``` bash 
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
La API quedará accesible en: http://127.0.0.1:8000/
**ENDPOINTS DETECTADOS**
- `GET /`  
  Root

- `POST /users`  
  Crear usuario — Body: `username`, `password`, `email?`, `is_active?`

- `GET /users`  
  Listar usuarios (devuelve datos "seguros" sin la contraseña)

- `GET /users/{user_id}`  
  Obtener usuario por id

- `PUT /users/{user_id}`  
  Actualizar usuario — Campos: `username`, `email`, `is_active`

- `DELETE /users/{user_id}`  
  Eliminar usuario

- `POST /login`  
  Login con `username` + `password`
