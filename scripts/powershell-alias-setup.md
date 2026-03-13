# Alias PowerShell para Release Rapido

## 1) Abrir perfil de PowerShell

Ejecuta:

```powershell
if (!(Test-Path -Path $PROFILE)) { New-Item -ItemType File -Path $PROFILE -Force }
notepad $PROFILE
```

## 2) Agregar alias de funcion

Pega este bloque al final del perfil y guarda:

```powershell
function dvch-release {
  Push-Location "c:\Users\LENOVO\Desktop\diego vasquez site\diego-vch-portfolio-site"
  try {
    powershell -NoProfile -ExecutionPolicy Bypass -File ".\\scripts\\release-and-open.ps1"
  }
  finally {
    Pop-Location
  }
}
```

## 3) Recargar perfil

```powershell
. $PROFILE
```

## 4) Usar alias

```powershell
dvch-release
```

Esto ejecuta:
1. `npm run release`
2. apertura de `https://diego-vasquez-chavez-site.vercel.app/`

