param(
  [string]$InputImage = "assets/diego-hero-alt.jpg",
  [string]$OutputBase = "assets/diego-hero-alt",
  [int]$WebpQuality = 82,
  [int]$AvifQuality = 56,
  [int]$Effort = 6
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command npx.cmd -ErrorAction SilentlyContinue)) {
  throw "npx.cmd no esta disponible. Instala Node.js para ejecutar este script."
}

if (-not (Test-Path $InputImage)) {
  throw "No se encontro la imagen de entrada: $InputImage"
}

Write-Output "Generando WebP..."
npx.cmd --yes sharp-cli -i $InputImage -o "$OutputBase.webp" -f webp -q $WebpQuality --effort $Effort | Out-Null

Write-Output "Generando AVIF..."
npx.cmd --yes sharp-cli -i $InputImage -o "$OutputBase.avif" -f avif -q $AvifQuality --effort $Effort | Out-Null

Write-Output "Listo. Archivos creados:"
Get-ChildItem "$OutputBase.*" | Select-Object Name, Length
