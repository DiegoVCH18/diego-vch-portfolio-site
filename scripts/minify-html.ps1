param(
  [string]$OutputDir = "dist"
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command npx.cmd -ErrorAction SilentlyContinue)) {
  throw "npx.cmd no esta disponible. Instala Node.js para ejecutar este script."
}

$targets = @(
  "index.html",
  "projects.html",
  "proyectos/iahorra-certus.html",
  "proyectos/academic-performance-prediction.html",
  "proyectos/customer-experience-loyalty-dashboard.html",
  "proyectos/automatizacion-reportes-mibanco.html"
)

foreach ($target in $targets) {
  if (-not (Test-Path $target)) {
    Write-Warning "No existe $target. Se omite."
    continue
  }

  $dest = Join-Path $OutputDir $target
  $destDir = Split-Path $dest -Parent
  if (-not (Test-Path $destDir)) {
    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
  }

  npx.cmd --yes html-minifier-terser `
    --collapse-whitespace `
    --remove-comments `
    --remove-redundant-attributes `
    --remove-script-type-attributes `
    --remove-style-link-type-attributes `
    --minify-css true `
    --minify-js true `
    "$target" `
    -o "$dest" | Out-Null

  Write-Output "Minificado: $target -> $dest"
}

Write-Output "Proceso completado."
