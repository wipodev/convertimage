from PIL import Image
from pathlib import Path
import io
from src.config import EXTENSIONS
from src.helper import show_help

def get_optimized_preview_data(input_path: str, quality: int):
    """Genera la imagen en memoria y devuelve (bytes, peso_kb)."""
    p = Path(input_path)
    ext = p.suffix.lower()
    
    format_map = {'.jpg': 'JPEG', '.jpeg': 'JPEG', '.png': 'PNG', '.webp': 'WEBP'}
    fmt = format_map.get(ext, 'PNG')

    with Image.open(p) as img:
        buffer = io.BytesIO()
        save_params = {"optimize": True}
        if fmt in ['JPEG', 'WEBP']:
            save_params["quality"] = quality
            
        img.save(buffer, format=fmt, **save_params)
        data = buffer.getvalue()
        size_kb = len(data) / 1024
        
    return data, size_kb

def optimize_file(input_path: str, quality: int = 80, output_name: str | None = None) -> Path:
    """Guarda el archivo final en disco."""
    p = Path(input_path)
    output_path = p.parent / f"{output_name if output_name else p.stem + '_optimizada'}{p.suffix}"
    
    # Reutilizamos la lógica de previsualización para obtener los bytes finales
    data, _ = get_optimized_preview_data(input_path, quality)
    
    with open(output_path, "wb") as f:
        f.write(data)
            
    return output_path

def start_optimize_files(args):
    file_paths = []
    quality = 80
    output_name = None

    for a in args:
        if a.isdigit():
            quality = int(a)
        elif Path(a).exists() and Path(a).suffix.lower()[1:] in EXTENSIONS:
            file_paths.append(a)
        else:
            output_name = a

    if not file_paths:
        print("No se encontraron imágenes válidas para optimizar.")
        show_help()
        return
    if len(file_paths) > 1:
        output_name = None
    
    print(f"Iniciando optimización flash (Calidad: {quality}%)...")
    for path in file_paths:
        try:
            result = optimize_file(path, quality, output_name)
            print(f"✓ Optimizado: {Path(path).name} -> {result.name}")
        except Exception as e:
            print(f"✗ Error en {Path(path).name}: {e}")
            show_help()
    return