from src.config import COMMANDS, EXTENSIONS

def show_help():
  print("ImageToolkit - Herramienta de procesamiento de imágenes\n")
  print("USO:")
  print("  imagetoolkit <comando> [opciones]\n")
  print("COMANDOS:\n")
  print("  -c, --convert <image_path> <extension>")
  print("      Convierte una imagen al formato indicado.")
  print("      Ejemplo:")
  print("        imagetoolkit -c ./foto.png jpg\n")
  print("  -p, --pack <folder_path> [dll_name]")
  print("      Convierte todos los iconos de una carpeta en un DLL")
  print("      de recursos de iconos para Windows.")
  print("      Si no se especifica dll_name, se usará el nombre")
  print("      de la carpeta.")
  print("      Ejemplo:")
  print("        imagetoolkit -p ./icons")
  print("        imagetoolkit -p ./icons MyIcons\n")
  print("NOTAS:")
  print("  - Las extensiones de imagen no deben incluir el punto.")
  print("  - Los comandos no distinguen entre mayúsculas y minúsculas.")


def is_command(arg: str, command: str) -> bool:
  if not arg:
    return False
  
  return arg in COMMANDS.get(command, [])

def is_image_extension(ext: str) -> bool:
  if not ext:
    return False

  ext = ext.lower().lstrip('.')
  return ext in EXTENSIONS