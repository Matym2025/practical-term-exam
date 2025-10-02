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

