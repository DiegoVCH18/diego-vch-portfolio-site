$ErrorActionPreference = "Stop"

Write-Output "[1/4] Verificando herramientas..."
if (-not (Get-Command npm.cmd -ErrorAction SilentlyContinue)) {
  throw "npm.cmd no esta disponible. Instala Node.js y reintenta."
}
if (-not (Get-Command npx.cmd -ErrorAction SilentlyContinue)) {
  throw "npx.cmd no esta disponible. Instala Node.js y reintenta."
}

Write-Output "[2/4] Optimizando imagenes (AVIF/WebP)..."
powershell -NoProfile -ExecutionPolicy Bypass -File ".\scripts\optimize-assets.ps1"

Write-Output "[3/4] Generando build de produccion en dist..."
npm.cmd run build

Write-Output "[4/4] Validando archivos criticos..."
$requiredFiles = @(
  "dist/index.html",
  "dist/projects.html",
  "dist/proyectos/iahorra-certus.html",
  "dist/proyectos/academic-performance-prediction.html",
  "dist/proyectos/customer-experience-loyalty-dashboard.html",
  "dist/proyectos/automatizacion-reportes-mibanco.html",
  "dist/proyectos/minimarket-aurelion.html",
  "dist/assets/diego-hero-alt.avif",
  "dist/assets/diego-hero-alt.webp",
  "dist/assets/CV_Diego_Vasquez.pdf"
)

$missing = @()
foreach ($file in $requiredFiles) {
  if (-not (Test-Path $file)) {
    $missing += $file
  }
}

if ($missing.Count -gt 0) {
  Write-Output "Faltan archivos requeridos en dist:"
  $missing | ForEach-Object { Write-Output " - $_" }
  throw "Validacion de release fallida"
}

Write-Output "Release listo. dist generado y validado correctamente."
