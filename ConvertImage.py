from pathlib import Path
from PIL import Image
import traceback
import sys

def convert_to(image_path: str, target_format: str) -> None:
    """
    Convierte una imagen a un formato específico de forma universal.
    
    Args:
        image_path: Ruta del archivo original.
        target_format: Formato de destino (ej. 'jpg', 'png', 'ico').
    """
    try:
        input_file = Path(image_path)
        if not input_file.exists():
            raise FileNotFoundError(f"Archivo no encontrado: {image_path}")

        # 1. Normalización del formato
        # Pillow prefiere 'JPEG' en lugar de 'JPG'
        fmt = target_format.upper()
        if fmt == "JPG":
            fmt = "JPEG"
            
        output_file = input_file.with_suffix(f".{target_format.lower()}")
        
        with Image.open(input_file) as img:
            # 2. Manejo de transparencia (Conversión de RGBA a RGB)
            # Si el destino es JPEG, debemos quitar la transparencia
            if fmt == "JPEG" and img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # 3. Preparación de argumentos de guardado
            save_args = {"quality": 85}
            
            # Solo añadir tamaños si es un archivo de icono (.ico)
            if fmt == "ICO":
                icon_sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]
                save_args["sizes"] = icon_sizes

            # 4. Guardado final
            img.save(output_file, fmt, **save_args)
            print(f"Éxito: Convertido a {output_file}")

    except Exception:
        log_file = Path(__file__).with_name("convert_error.log")
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"\nError convirtiendo {image_path}:\n")
            traceback.print_exc(file=f)
        print("Error: Revisa 'convert_error.log' para más detalles.")

if __name__ == "__main__":
    # Uso: python script.py png imagen.jpg
    if len(sys.argv) >= 3:
        convert_to(sys.argv[2], sys.argv[1])
    else:
        print("Uso: python script.py [formato_destino] [ruta_imagen]")