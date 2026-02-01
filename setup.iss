[Setup]
AppName=Convert Image
AppVersion=1.0
DefaultDirName={autopf}\Convert Image
DefaultGroupName=Convert Image
SetupIconFile=icon.ico
UninstallDisplayIcon={app}\ConvertImage.exe
Compression=lzma
LicenseFile=LICENSE
SolidCompression=yes
OutputDir=dist
OutputBaseFilename=ConvertImage_Installer
ArchitecturesInstallIn64BitMode=x64compatible

[Files]
Source: "dist\ConvertImage.exe"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Convert Image"; Filename: "{app}\ConvertImage.exe"

[Registry]
; --- SOPORTE PARA .PNG ---
Root: HKCR; Subkey: "SystemFileAssociations\.png\shell\ConvertImageMenu"; ValueType: string; ValueName: "MUIVerb"; ValueData: "Convert Image"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.png\shell\ConvertImageMenu"; ValueType: string; ValueName: "SubCommands"; ValueData: ""; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.png\shell\ConvertImageMenu"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\ConvertImage.exe"; Flags: uninsdeletekey

; Submenús para .PNG
Root: HKCR; Subkey: "SystemFileAssociations\.png\shell\ConvertImageMenu\shell\01_ico"; ValueType: string; ValueData: "Convertir a Icono (.ico)"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.png\shell\ConvertImageMenu\shell\01_ico"; ValueType: string; ValueName: "Icon"; ValueData: "imageres.dll,197"
Root: HKCR; Subkey: "SystemFileAssociations\.png\shell\ConvertImageMenu\shell\01_ico\command"; ValueType: string; ValueData: """{app}\ConvertImage.exe"" ico ""%1"""; Flags: uninsdeletekey

Root: HKCR; Subkey: "SystemFileAssociations\.png\shell\ConvertImageMenu\shell\02_jpg"; ValueType: string; ValueData: "Convertir a Imagen (.jpg)"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.png\shell\ConvertImageMenu\shell\02_jpg"; ValueType: string; ValueName: "Icon"; ValueData: "imageres.dll,72"
Root: HKCR; Subkey: "SystemFileAssociations\.png\shell\ConvertImageMenu\shell\02_jpg\command"; ValueType: string; ValueData: """{app}\ConvertImage.exe"" jpg ""%1"""; Flags: uninsdeletekey

Root: HKCR; Subkey: "SystemFileAssociations\.png\shell\ConvertImageMenu\shell\03_webp"; ValueType: string; ValueData: "Convertir a Imagen (.webp)"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.png\shell\ConvertImageMenu\shell\03_webp"; ValueType: string; ValueName: "Icon"; ValueData: "imageres.dll,11"
Root: HKCR; Subkey: "SystemFileAssociations\.png\shell\ConvertImageMenu\shell\03_webp\command"; ValueType: string; ValueData: """{app}\ConvertImage.exe"" webp ""%1"""; Flags: uninsdeletekey

; --- SOPORTE PARA .JPG ---
Root: HKCR; Subkey: "SystemFileAssociations\.jpg\shell\ConvertImageMenu"; ValueType: string; ValueName: "MUIVerb"; ValueData: "Convert Image"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.jpg\shell\ConvertImageMenu"; ValueType: string; ValueName: "SubCommands"; ValueData: ""; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.jpg\shell\ConvertImageMenu"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\ConvertImage.exe"; Flags: uninsdeletekey

; Submenús para .JPG
Root: HKCR; Subkey: "SystemFileAssociations\.jpg\shell\ConvertImageMenu\shell\01_ico"; ValueType: string; ValueData: "Convertir a Icono (.ico)"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.jpg\shell\ConvertImageMenu\shell\01_ico"; ValueType: string; ValueName: "Icon"; ValueData: "imageres.dll,197"
Root: HKCR; Subkey: "SystemFileAssociations\.jpg\shell\ConvertImageMenu\shell\01_ico\command"; ValueType: string; ValueData: """{app}\ConvertImage.exe"" ico ""%1"""; Flags: uninsdeletekey

Root: HKCR; Subkey: "SystemFileAssociations\.jpg\shell\ConvertImageMenu\shell\02_png"; ValueType: string; ValueData: "Convertir a Imagen (.png)"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.jpg\shell\ConvertImageMenu\shell\02_png"; ValueType: string; ValueName: "Icon"; ValueData: "imageres.dll,71"
Root: HKCR; Subkey: "SystemFileAssociations\.jpg\shell\ConvertImageMenu\shell\02_png\command"; ValueType: string; ValueData: """{app}\ConvertImage.exe"" png ""%1"""; Flags: uninsdeletekey

Root: HKCR; Subkey: "SystemFileAssociations\.jpg\shell\ConvertImageMenu\shell\03_webp"; ValueType: string; ValueData: "Convertir a Imagen (.webp)"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.jpg\shell\ConvertImageMenu\shell\03_webp"; ValueType: string; ValueName: "Icon"; ValueData: "imageres.dll,11"
Root: HKCR; Subkey: "SystemFileAssociations\.jpg\shell\ConvertImageMenu\shell\03_webp\command"; ValueType: string; ValueData: """{app}\ConvertImage.exe"" webp ""%1"""; Flags: uninsdeletekey

; --- SOPORTE PARA .WEBP ---
Root: HKCR; Subkey: "SystemFileAssociations\.webp\shell\ConvertImageMenu"; ValueType: string; ValueName: "MUIVerb"; ValueData: "Convert Image"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.webp\shell\ConvertImageMenu"; ValueType: string; ValueName: "SubCommands"; ValueData: ""; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.webp\shell\ConvertImageMenu"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\ConvertImage.exe"; Flags: uninsdeletekey

; Submenús para .WEBP
Root: HKCR; Subkey: "SystemFileAssociations\.webp\shell\ConvertImageMenu\shell\01_ico"; ValueType: string; ValueData: "Convertir a Icono (.ico)"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.webp\shell\ConvertImageMenu\shell\01_ico"; ValueType: string; ValueName: "Icon"; ValueData: "imageres.dll,197"
Root: HKCR; Subkey: "SystemFileAssociations\.webp\shell\ConvertImageMenu\shell\01_ico\command"; ValueType: string; ValueData: """{app}\ConvertImage.exe"" ico ""%1"""; Flags: uninsdeletekey

Root: HKCR; Subkey: "SystemFileAssociations\.webp\shell\ConvertImageMenu\shell\02_png"; ValueType: string; ValueData: "Convertir a Imagen (.png)"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.webp\shell\ConvertImageMenu\shell\02_png"; ValueType: string; ValueName: "Icon"; ValueData: "imageres.dll,71"
Root: HKCR; Subkey: "SystemFileAssociations\.webp\shell\ConvertImageMenu\shell\02_png\command"; ValueType: string; ValueData: """{app}\ConvertImage.exe"" png ""%1"""; Flags: uninsdeletekey

Root: HKCR; Subkey: "SystemFileAssociations\.webp\shell\ConvertImageMenu\shell\03_jpg"; ValueType: string; ValueData: "Convertir a Imagen (.jpg)"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.webp\shell\ConvertImageMenu\shell\03_jpg"; ValueType: string; ValueName: "Icon"; ValueData: "imageres.dll,72"
Root: HKCR; Subkey: "SystemFileAssociations\.webp\shell\ConvertImageMenu\shell\03_jpg\command"; ValueType: string; ValueData: """{app}\ConvertImage.exe"" jpg ""%1"""; Flags: uninsdeletekey

; --- SOPORTE PARA .ICO ---
Root: HKCR; Subkey: "SystemFileAssociations\.ico\shell\ConvertImageMenu"; ValueType: string; ValueName: "MUIVerb"; ValueData: "Convert Image"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.ico\shell\ConvertImageMenu"; ValueType: string; ValueName: "SubCommands"; ValueData: ""; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.ico\shell\ConvertImageMenu"; ValueType: string; ValueName: "Icon"; ValueData: "{app}\ConvertImage.exe"; Flags: uninsdeletekey

; Submenús para .ICO
Root: HKCR; Subkey: "SystemFileAssociations\.ico\shell\ConvertImageMenu\shell\01_png"; ValueType: string; ValueData: "Convertir a Imagen (.png)"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.ico\shell\ConvertImageMenu\shell\01_png"; ValueType: string; ValueName: "Icon"; ValueData: "imageres.dll,71"
Root: HKCR; Subkey: "SystemFileAssociations\.ico\shell\ConvertImageMenu\shell\01_png\command"; ValueType: string; ValueData: """{app}\ConvertImage.exe"" png ""%1"""; Flags: uninsdeletekey

Root: HKCR; Subkey: "SystemFileAssociations\.ico\shell\ConvertImageMenu\shell\02_jpg"; ValueType: string; ValueData: "Convertir a Imagen (.jpg)"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.ico\shell\ConvertImageMenu\shell\02_jpg"; ValueType: string; ValueName: "Icon"; ValueData: "imageres.dll,72"
Root: HKCR; Subkey: "SystemFileAssociations\.ico\shell\ConvertImageMenu\shell\02_jpg\command"; ValueType: string; ValueData: """{app}\ConvertImage.exe"" jpg ""%1"""; Flags: uninsdeletekey

Root: HKCR; Subkey: "SystemFileAssociations\.ico\shell\ConvertImageMenu\shell\03_webp"; ValueType: string; ValueData: "Convertir a Imagen (.webp)"; Flags: uninsdeletekey
Root: HKCR; Subkey: "SystemFileAssociations\.ico\shell\ConvertImageMenu\shell\03_webp"; ValueType: string; ValueName: "Icon"; ValueData: "imageres.dll,11"
Root: HKCR; Subkey: "SystemFileAssociations\.ico\shell\ConvertImageMenu\shell\03_webp\command"; ValueType: string; ValueData: """{app}\ConvertImage.exe"" webp ""%1"""; Flags: uninsdeletekey