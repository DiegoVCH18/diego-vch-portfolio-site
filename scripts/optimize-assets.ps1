param(
  [int]$WebpQuality = 82,
  [int]$AvifQuality = 56,
  [int]$Effort = 6
)

$ErrorActionPreference = "Stop"

if (-not (Get-Command npx.cmd -ErrorAction SilentlyContinue)) {
  throw "npx.cmd no esta disponible. Instala Node.js para ejecutar este script."
}

$targets = @(
  @{ Input = "assets/diego-hero-alt.jpg"; Base = "assets/diego-hero-alt" },
  @{ Input = "assets/logo-personal.jpg"; Base = "assets/logo-personal" },
  @{ Input = "assets/logo.jpg"; Base = "assets/logo" },
  @{ Input = "assets/logos.jpg"; Base = "assets/logos" }
)

foreach ($item in $targets) {
  if (-not (Test-Path $item.Input)) {
    Write-Warning "No se encontro: $($item.Input). Se omite."
    continue
  }

  Write-Output "Optimizando $($item.Input) -> WebP"
  npx.cmd --yes sharp-cli -i $item.Input -o "$($item.Base).webp" -f webp -q $WebpQuality --effort $Effort | Out-Null

  Write-Output "Optimizando $($item.Input) -> AVIF"
  npx.cmd --yes sharp-cli -i $item.Input -o "$($item.Base).avif" -f avif -q $AvifQuality --effort $Effort | Out-Null
}

Write-Output "Archivos optimizados:"
Get-ChildItem assets\*.avif, assets\*.webp | Select-Object Name, Length | Sort-Object Name
