import os
import subprocess
import shutil
from pathlib import Path
from src.pack import pack

# --- CONFIGURACIÓN DE RUTAS ---
# Obtenemos el APPDATA del sistema
APPDATA = os.environ.get('LOCALAPPDATA')
INNO_SETUP_EXE = Path(APPDATA) / "Programs/Inno Setup 6/ISCC.exe"

# Rutas del proyecto
BASE_DIR = Path(__file__).parent
SPEC_FILE = BASE_DIR / "app.spec"
ISS_FILE = BASE_DIR / "setup.iss"

def clean_folders():
    """Elimina carpetas de compilaciones anteriores para evitar basura."""
    folders = [BASE_DIR / "dist", BASE_DIR / "build"]
    for folder in folders:
        if folder.exists():
            print(f"[*] Limpiando {folder.name}...")
            shutil.rmtree(folder)

def run_pyinstaller():
    """Ejecuta PyInstaller usando el archivo .spec."""
    print("[*] Iniciando PyInstaller...")
    try:
        subprocess.run(["pyinstaller", str(SPEC_FILE)], check=True)
        print("[+] PyInstaller terminó con éxito.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error en PyInstaller: {e}")
        exit(1)

def run_inno_setup():
    """Ejecuta el compilador de Inno Setup."""
    print("[*] Iniciando Inno Setup...")
    if not INNO_SETUP_EXE.exists():
        print(f"[-] Error: No se encontró ISCC.exe en {INNO_SETUP_EXE}")
        exit(1)
    
    try:
        # Ejecutamos: ISCC.exe installer_script.iss
        subprocess.run([str(INNO_SETUP_EXE), str(ISS_FILE)], check=True)
        print("[+] Instalador generado con éxito.")
    except subprocess.CalledProcessError as e:
        print(f"[-] Error en Inno Setup: {e}")
        exit(1)

if __name__ == "__main__":
    print("--- INICIANDO PROCESO DE BUILD ---")
    clean_folders()
    run_pyinstaller()
    pack("assets", "dist/imagetoolkit")
    run_inno_setup()
    print("--- PROCESO FINALIZADO ---")