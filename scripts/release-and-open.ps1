param(
  [string]$ProductionUrl = "https://diego-vasquez-chavez-site.vercel.app/"
)

$ErrorActionPreference = "Stop"

Write-Output "Ejecutando flujo release..."
npm.cmd run release

Write-Output "Abriendo produccion..."
Start-Process $ProductionUrl

Write-Output "Proceso completado."
