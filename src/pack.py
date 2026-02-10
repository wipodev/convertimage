import os
import sys, re
import subprocess
import tempfile
from pathlib import Path
from src.helper import show_help
from src.config import RC_CONTENT, RC_PATH, LINK_PATH

def create_icon_pack(icons_path: str, output_name: str) -> None:
    output_dll = icons_path.parent / f"{output_name}.dll"
    raw_icons = [f for f in os.listdir(icons_path) if f.endswith('.ico')]

    def natural_sort_key(s):
        return [int(text) if text.isdigit() else text.lower() 
                for text in re.split(r'(\d+)', s)]
    
    icons = sorted(raw_icons, key=natural_sort_key)

    if not icons:
        print("No se encontraron iconos .ico")
        return

    # 1. Crear carpeta temporal única
    with tempfile.TemporaryDirectory() as tmp_dir:
        tmp_path = Path(tmp_dir)
        rc_file = tmp_path / "resource.rc"
        res_file = tmp_path / "resource.res"

        # 2. Generar el contenido del .rc
        rc_content = RC_CONTENT.format(output_name=output_name)
        for i, icon in enumerate(icons):
            # Usamos la ruta absoluta del icono y escapamos las barras para el .rc
            ruta_icon_abs = (icons_path / icon).as_posix()
            rc_content += f"{i + 100} ICON \"{ruta_icon_abs}\"\n"

        rc_file.write_text(rc_content, encoding="utf-8")

        try:
            print(f"--- Iniciando compilación en: {tmp_dir} ---")
            
            # 3. Compilar .rc a .res
            # Forzamos a RC a escribir el output en nuestra carpeta temporal
            subprocess.run([
                str(RC_PATH), 
                f"/fo{res_file}", # Flag /fo especifica el archivo de salida
                str(rc_file)
            ], check=True, cwd=str(RC_PATH.parent))

            print("--- Resource.res creado con éxito. ---")
            
            # 4. Enlazar .res a .dll
            subprocess.run([
                str(LINK_PATH), "/DLL", "/NOENTRY", "/MACHINE:X64", 
                str(res_file), 
                f"/OUT:{str(output_dll)}"
            ], check=True, cwd=str(LINK_PATH.parent))

            print(f"\n¡Éxito! Archivo generado: {output_dll}")

        except subprocess.CalledProcessError as e:
            print(f"\nError en el subproceso: {e}")
        except Exception as e:
            print(f"\nError inesperado: {e}")

def pack(icons_path: str, dll_name: str | None = None) -> None:
  icons_path = Path(icons_path).resolve()
  if not icons_path.is_dir():
    print("La ruta no es un directorio.")
    show_help()
    return
  output_name = dll_name.strip() if dll_name and dll_name.strip() else icons_path.name
  create_icon_pack(icons_path, output_name)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        show_help()
    else:
        dll_name = sys.argv[2] if len(sys.argv) >= 3 else None
        pack(sys.argv[1], dll_name)