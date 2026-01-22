Instalación
- Clona el repositorio o copia los archivos en tu máquina.
- Crea un entorno virtual en la carpeta del proyecto:
py -m venv .venv
- Activa el entorno virtual:
- PowerShell:
.\.venv\Scripts\Activate.ps1
- CMD:
.\.venv\Scripts\activate.bat
- Git Bash:
source .venv/Scripts/activate
- Instala las dependencias:
pip install fastapi uvicorn



▶️ Ejecución
Inicia el servidor con:
uvicorn main:app --reload


- La API estará disponible en: http://127.0.0.1:8000
- La documentación interactiva en:
- Swagger UI → http://127.0.0.1:8000/docs
- ReDoc → http://127.0.0.1:8000/redoc


