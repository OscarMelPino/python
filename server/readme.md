# Instalación
- Abrir consola e ir a la carpeta
- pip install virtualenv (si no estaba instalado)
- python -m virtualenv venv

# Activar virtualenv
- Mac: source venv/bin/activate
- Windows: venv/scripts/activate
    Comprobar policy de ejecución de scripts:
    Get-ExecutionPolicy
    Si está restringida la ejecución de scripts:
    Set-ExecutionPolicy Unrestricted

# Instalar dependencias
- Activar venv
- pip install -r requirements.txt

# Lanzar servidor
- Activar env
- python application.py

# Desactivar virtualenv
- deactivate
