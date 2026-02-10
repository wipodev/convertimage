; 1. DEFINICIONES DE VARIABLES
#define APP_NAME "Image Toolkit"
#define APP_SUBKEY "ImageToolKit"
#define APP_EXE "{app}\ImageToolkit.exe"
#define ICON_DLL "{app}\ImageToolkit.dll"
#define CMD_STORE "SOFTWARE\Microsoft\Windows\CurrentVersion\Explorer\CommandStore\shell\ITK."

[Setup]
AppName={#APP_NAME}
AppVersion=1.1.0
AppPublisher=WipoDev
AppPublisherURL=https://github.com/wipodev/ImageToolkit
AppSupportURL=https://github.com/wipodev/ImageToolkit/issues
AppUpdatesURL=https://github.com/wipodev/ImageToolkit/releases
VersionInfoCompany=WipoDev
VersionInfoCopyright=© 2026 WipoDev. Apache 2.0 License.
VersionInfoDescription=Instalador de {#APP_NAME}
VersionInfoProductName={#APP_NAME}
VersionInfoProductVersion=1.1.0.0
VersionInfoTextVersion=1.1.0.0
VersionInfoVersion=1.1.0.0
DefaultDirName={autopf}\{#APP_NAME}
DefaultGroupName={#APP_NAME}
SetupIconFile=assets\itk1.ico
UninstallDisplayIcon={app}\ImageToolkit.exe
Compression=lzma
LicenseFile=LICENSE
SolidCompression=yes
OutputDir=dist
OutputBaseFilename=ImageToolkit_Installer
ArchitecturesInstallIn64BitMode=x64compatible

[Files]
Source: "dist\ImageToolkit.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "dist\ImageToolkit.dll"; DestDir: "{app}"; Flags: ignoreversion
Source: "tools\*"; DestDir: "{app}\tools"; Flags: ignoreversion recursesubdirs createallsubdirs

[Icons]
Name: "{group}\{#APP_NAME}"; Filename: "{#ICON_DLL},0"

[Registry]
; ##########################################################################
; ===========================================================================
; 1. ALMACÉN DE COMANDOS (CommandStore) con Iconos Individuales
; ===========================================================================

; --- Conversiones ---
Root: HKLM; Subkey: "{#CMD_STORE}ico"; ValueType: string; ValueName: ""; ValueData: "Convertir a ICO"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}ico"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},2"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}ico\command"; ValueType: string; ValueName: ""; ValueData: """{#APP_EXE}"" -c ico ""%1"""; Flags: uninsdeletekey

Root: HKLM; Subkey: "{#CMD_STORE}png"; ValueType: string; ValueName: ""; ValueData: "Convertir a PNG"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}png"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},3"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}png\command"; ValueType: string; ValueName: ""; ValueData: """{#APP_EXE}"" -c png ""%1"""; Flags: uninsdeletekey

Root: HKLM; Subkey: "{#CMD_STORE}jpg"; ValueType: string; ValueName: ""; ValueData: "Convertir a JPG"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}jpg"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},4"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}jpg\command"; ValueType: string; ValueName: ""; ValueData: """{#APP_EXE}"" -c jpg ""%1"""; Flags: uninsdeletekey

Root: HKLM; Subkey: "{#CMD_STORE}webp"; ValueType: string; ValueName: ""; ValueData: "Convertir a WEBP"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}webp"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},5"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}webp\command"; ValueType: string; ValueName: ""; ValueData: """{#APP_EXE}"" -c webp ""%1"""; Flags: uninsdeletekey

Root: HKLM; Subkey: "{#CMD_STORE}bmp"; ValueType: string; ValueName: ""; ValueData: "Convertir a BMP"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}bmp"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},6"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}bmp\command"; ValueType: string; ValueName: ""; ValueData: """{#APP_EXE}"" -c bmp ""%1"""; Flags: uninsdeletekey

Root: HKLM; Subkey: "{#CMD_STORE}tiff"; ValueType: string; ValueName: ""; ValueData: "Convertir a TIFF"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}tiff"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},7"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}tiff\command"; ValueType: string; ValueName: ""; ValueData: """{#APP_EXE}"" -c tiff ""%1"""; Flags: uninsdeletekey

; --- Herramientas ---
Root: HKLM; Subkey: "{#CMD_STORE}resize"; ValueType: string; ValueData: "Redimensionar imagen"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}resize"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},8"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}resize\command"; ValueType: string; ValueData: """{#APP_EXE}"" -r ""%1"""; Flags: uninsdeletekey

Root: HKLM; Subkey: "{#CMD_STORE}cut"; ValueType: string; ValueData: "Recortar imagen"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}cut"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},9"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}cut\command"; ValueType: string; ValueData: """{#APP_EXE}"" -x ""%1"""; Flags: uninsdeletekey

Root: HKLM; Subkey: "{#CMD_STORE}opt"; ValueType: string; ValueData: "Optimizar imagen"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}opt"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},10"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}opt\command"; ValueType: string; ValueData: """{#APP_EXE}"" -o ""%1"""; Flags: uninsdeletekey

Root: HKLM; Subkey: "{#CMD_STORE}opt_def"; ValueType: string; ValueData: "Optimizar imagen (predeterminado)"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}opt_def"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},11"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}opt_def\command"; ValueType: string; ValueData: """{#APP_EXE}"" -od ""%1"""; Flags: uninsdeletekey

Root: HKLM; Subkey: "{#CMD_STORE}pack"; ValueType: string; ValueData: "Empaquetar imágenes (DLL Resource)"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}pack"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},12"; Flags: uninsdeletekey
Root: HKLM; Subkey: "{#CMD_STORE}pack\command"; ValueType: string; ValueData: """{#APP_EXE}"" -p ""%1"""; Flags: uninsdeletekey

; ===========================================================================
; 2. ASOCIACIONES POR EXTENSIÓN (IMÁGENES)
; ===========================================================================
Root: HKCR; Subkey: "SystemFileAssociations\.ico\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "MUIVerb"; ValueData: "{#APP_NAME}"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.ico\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},0"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.ico\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "SubCommands"; ValueData: "ITK.jpg;ITK.png;ITK.webp;ITK.bmp;ITK.tiff;|;ITK.resize;ITK.opt;ITK.opt_def;ITK.cut"; Flags: uninsdeletekey

Root: HKCR; Subkey: "SystemFileAssociations\.jpg\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "MUIVerb"; ValueData: "{#APP_NAME}"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.jpg\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},0"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.jpg\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "SubCommands"; ValueData: "ITK.ico;ITK.png;ITK.webp;ITK.bmp;ITK.tiff;|;ITK.resize;ITK.opt;ITK.opt_def;ITK.cut"; Flags: uninsdeletekey

Root: HKCR; Subkey: "SystemFileAssociations\.jpeg\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "MUIVerb"; ValueData: "{#APP_NAME}"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.jpeg\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},0"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.jpeg\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "SubCommands"; ValueData: "ITK.ico;ITK.png;ITK.webp;ITK.bmp;ITK.tiff;|;ITK.resize;ITK.opt;ITK.opt_def;ITK.cut"; Flags: uninsdeletekey

Root: HKCR; Subkey: "SystemFileAssociations\.png\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "MUIVerb"; ValueData: "{#APP_NAME}"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.png\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},0"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.png\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "SubCommands"; ValueData: "ITK.ico;ITK.jpg;ITK.webp;ITK.bmp;ITK.tiff;|;ITK.resize;ITK.opt;ITK.opt_def;ITK.cut"; Flags: uninsdeletekey

Root: HKCR; Subkey: "SystemFileAssociations\.webp\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "MUIVerb"; ValueData: "{#APP_NAME}"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.webp\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},0"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.webp\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "SubCommands"; ValueData: "ITK.ico;ITK.jpg;ITK.png;ITK.bmp;ITK.tiff;|;ITK.resize;ITK.opt;ITK.opt_def;ITK.cut"; Flags: uninsdeletekey

Root: HKCR; Subkey: "SystemFileAssociations\.bmp\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "MUIVerb"; ValueData: "{#APP_NAME}"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.bmp\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},0"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.bmp\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "SubCommands"; ValueData: "ITK.ico;ITK.jpg;ITK.png;ITK.webp;ITK.tiff;|;ITK.resize;ITK.opt;ITK.opt_def;ITK.cut"; Flags: uninsdeletekey

Root: HKCR; Subkey: "SystemFileAssociations\.tiff\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "MUIVerb"; ValueData: "{#APP_NAME}"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.tiff\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},0"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.tiff\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "SubCommands"; ValueData: "ITK.ico;ITK.jpg;ITK.png;ITK.webp;ITK.bmp;|;ITK.resize;ITK.opt;ITK.opt_def;ITK.cut"; Flags: uninsdeletekey

Root: HKCR; Subkey: "SystemFileAssociations\image\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "MUIVerb"; ValueData: "{#APP_NAME}"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\image\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},0"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\image\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "SubCommands"; ValueData: "ITK.ico;ITK.jpg;ITK.png;ITK.webp;ITK.bmp;ITK.tiff;|;ITK.resize;ITK.opt;ITK.opt_def;ITK.cut"; Flags: uninsdeletekey

; ===========================================================================
; 3. CARPETAS Y MULTISELECCIÓN
; ===========================================================================

; Directorios (Botón derecho sobre la carpeta)
Root: HKCR; Subkey: "Directory\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "MUIVerb"; ValueData: "{#APP_NAME}"; Flags: uninsdeletekey
Root: HKCR; Subkey: "Directory\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},0"; Flags: uninsdeletekey
Root: HKCR; Subkey: "Directory\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "SubCommands"; ValueData: "ITK.ico;ITK.jpg;ITK.png;ITK.webp;ITK.bmp;ITK.tiff;|;ITK.opt_def;ITK.pack"; Flags: uninsdeletekey

; Background (Fondo blanco de carpeta)
Root: HKCR; Subkey: "Directory\Background\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "MUIVerb"; ValueData: "{#APP_NAME}"; Flags: uninsdeletekey
Root: HKCR; Subkey: "Directory\Background\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "Icon"; ValueData: "{#ICON_DLL},0"; Flags: uninsdeletekey
Root: HKCR; Subkey: "Directory\Background\shell\{#APP_SUBKEY}"; ValueType: string; ValueName: "SubCommands"; ValueData: "ITK.ico;ITK.jpg;ITK.png;ITK.webp;ITK.bmp;ITK.tiff;|;ITK.opt_def;ITK.pack"; Flags: uninsdeletekey