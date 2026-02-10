from pathlib import Path
import sys

BASE_DIR = Path(sys.executable).parent if getattr(sys, 'frozen', False) else Path(__file__).parent.parent

RC_PATH = BASE_DIR / "tools" / "rc.exe"
LINK_PATH = BASE_DIR / "tools" / "link.exe"

COMMANDS = {
    "convert":          ["-c",  "--convert"],
    "resize":           ["-r",  "--resize"],
    "optimize":         ["-o",  "--optimize"],
    "optimize-default": ["-od", "--optimize-default"],
    "cut":              ["-x",  "--cut"],
    "svg":              ["-s",  "--svg"],
    "pack":             ["-p",  "--pack"],
    "help":             ["-h",  "--help"],
}

EXTENSIONS = {
  "ico", "jpg", "jpeg", "png", "gif", "bmp", "webp", "tiff", "svg"
}

RC_CONTENT = """
1 VERSIONINFO
FILEVERSION 1,0,0,0
PRODUCTVERSION 1,0,0,0
BEGIN
    BLOCK "StringFileInfo"
    BEGIN
        BLOCK "040904b0"
        BEGIN
            VALUE "CompanyName",      "wipodev"
            VALUE "FileDescription",  "Librería de iconos personalizada"
            VALUE "FileVersion",      "1.0.0.0"
            VALUE "InternalName",     "{output_name}"
            VALUE "ProductName",      "Icon Pack Generator"
        END
    END
    BLOCK "VarFileInfo"
    BEGIN
        VALUE "Translation", 0x409, 1200
    END
END
"""