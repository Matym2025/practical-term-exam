Practical Term Exam 

Este repositorio contiene una API REST (FastAPI) para manejo básico de usuarios (CRUD) y autenticación. Incluye un script brute.sh pensado para pruebas locales (simula intentos de login).

Archivos ajuntos para el funcionamiento del programa

main.py — implementación FastAPI con modelos en sqlmodel y almacenamiento en memoria (users_db).

brute.sh — script bash que prueba múltiples contraseñas contra http://127.0.0.1:8000/

requirements.txt — dependencias: fastapi, uvicorn, sqlmodel.

Estructura (actual)
practical-term-exam/
├── main.py
├── brute.sh
├── requirements.txt
└── (otros archivos opcionales)
Requisitos y preparación

Python 3.10+

pip

Se recomienda crear un entorno virtual:

Windows (PowerShell)

python -m venv venv
venv\Scripts\Activate.ps1

Instalar dependencias:

pip install -r requirements.txt
Cómo ejecutar la API 

Desde la raíz del proyecto, con el entorno virtual activado:

uvicorn main:app --reload --host 0.0.0.0 --port 8000

La API quedará accesible en http://127.0.0.1:8000/.

Endpoints detectados 

GET / — root

POST /users — crear usuario (body: username, password, email?, is_active?)

GET /users — listar usuarios (devuelve datos "seguros" sin la contraseña)

GET /users/{user_id} — obtener usuario por id

PUT /users/{user_id} — actualizar usuario (username, email, is_active)

DELETE /users/{user_id} — eliminar usuario

POST /login — login con username + password

Ejemplo de login (body JSON):

{ "username": "matias", "password": "matym123" }

Respuesta satisfactoria actual:

{ "message": "login successful" }

Respuesta por credenciales inválidas:

{ "message": "Invalid credentials" }
