# 📸 Convert Image (Context Menu)

**Convert Image** es una herramienta profesional para Windows que permite convertir imágenes entre múltiples formatos (**PNG, JPG, WEBP e ICO**) directamente desde el menú contextual del explorador de archivos.

---

## ✨ Características

- **Integración Nativa**: Accede a las funciones con clic derecho.
- **Menú en Cascada**: Interfaz organizada y limpia en Windows.
- **Soporte Multiformato**: Conversión cruzada inteligente entre `.png`, `.jpg`, `.webp` y `.ico`.
- **Manejo de Transparencia**: Gestión automática de canales Alpha al convertir a formatos sin transparencia.
- **Generador de Iconos**: Crea archivos `.ico` optimizados con múltiples capas de resolución.

---

## 🚀 Instalación

1. Ve a la sección de **Releases** de este repositorio.
2. Descarga la última versión de **ConvertImage_Installer.exe**.
3. Ejecuta el instalador. ¡Listo! Ya puedes hacer clic derecho sobre tus imágenes.

---

## 🛠️ Desarrollo y Compilación

Si deseas contribuir o modificar el comportamiento del script, sigue estos pasos:

### 1. Clonar y configurar el entorno

Se recomienda encarecidamente el uso de un entorno virtual para mantener limpias las dependencias de tu sistema.

```bash
# Clonar el repositorio
git clone https://github.com/wipodev/convertimage.git
cd convertimage

# Crear entorno virtual
python -m venv venv

# Activar el entorno (Windows)
.\venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt
```

### 2. Estructura del Proyecto

- **ConvertImage.py**: Lógica principal de procesamiento (Pillow).
- **ConvertImage.spec**: Configuración de empaquetado para PyInstaller.
- **setup.iss**: Script de Inno Setup para el instalador y registro de Windows.
- **build.py**: Script de automatización total del proceso de construcción.

### 3. Compilación del Instalador

Para generar el ejecutable y el instalador final en un solo paso:

```bash
python build.py
```

> **Nota**: El instalador generado se guardará localmente en la carpeta `dist/`, la cual está excluida del control de versiones.

---

## 📄 Licencia

Este proyecto está bajo la **Licencia Apache 2.0**. Consulta el archivo `LICENSE` para más detalles.
