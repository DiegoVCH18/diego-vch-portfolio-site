# Release Checklist - Diego VCH Portfolio

## 1) Validacion Local (obligatorio)

1. Abre y revisa visualmente la portada:
   - index.html (menu movil, hero, formulario de briefing, logos)
2. Revisa pagina de proyectos y fichas:
   - projects.html
   - proyectos/iahorra-certus.html
   - proyectos/academic-performance-prediction.html
   - proyectos/customer-experience-loyalty-dashboard.html
   - proyectos/automatizacion-reportes-mibanco.html
3. Verifica que el CV abra correctamente:
   - assets/CV_Diego_Vasquez.pdf
4. Ejecuta el flujo completo:
   - npm run release
5. Confirma artefactos en dist:
   - dist/index.html
   - dist/projects.html
   - dist/proyectos/*
   - dist/assets/*

## 2) Control De Cambios

1. Revisa cambios:
   - git status
2. Verifica diff antes de commit:
   - git diff
3. Commit recomendado:
   - git add .
   - git commit -m "feat: optimize portfolio UX, SEO and release pipeline"

## 3) Publicacion A GitHub

1. Push a rama principal o rama de release:
   - git push origin main

## 4) Despliegue En Vercel

1. Verifica configuracion de proyecto:
   - Root Directory: diego-vch-portfolio-site
2. Verifica build:
   - Build Command: npm run build
   - Output Directory: dist
3. Espera deploy automatico despues del push.

## 5) Verificacion Post-Deploy

1. Revisa URLs clave en produccion:
   - /
   - /projects
   - /proyectos/iahorra-certus
   - /proyectos/academic-performance-prediction
   - /proyectos/customer-experience-loyalty-dashboard
   - /proyectos/automatizacion-reportes-mibanco
2. Revisa mobile:
   - menu hamburguesa
   - estado activo por seccion
   - formulario de briefing
3. Revisa recursos:
   - imagen hero (avif/webp fallback)
   - logos (avif/webp fallback)
   - descarga de CV
4. Revisa previews sociales:
   - Open Graph/Twitter en projects y cada ficha.

## 6) Rollback Rapido (si algo falla)

1. Revertir al commit anterior estable:
   - git revert <commit_hash>
2. Push del revert:
   - git push origin main
3. Confirmar redeploy correcto en Vercel.

## 7) Mantenimiento Recomendado

1. Si cambias fotos/logos, vuelve a optimizar:
   - powershell -NoProfile -ExecutionPolicy Bypass -File scripts/optimize-assets.ps1
2. Re-genera build de produccion:
   - npm run build
3. Para flujo completo:
   - npm run release
