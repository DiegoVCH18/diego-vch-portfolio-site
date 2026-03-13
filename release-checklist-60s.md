# Release Checklist 60s

## Pre-deploy (rapido)

1. Ejecutar release:
   - npm run release
2. Confirmar dist:
   - dist/index.html
   - dist/projects.html
   - dist/proyectos/*
   - dist/assets/CV_Diego_Vasquez.pdf

## Push

1. Revisar cambios:
   - git status
2. Commit:
   - git add .
   - git commit -m "chore: release portfolio"
3. Publicar:
   - git push origin main

## Verificacion post-deploy

1. Home y mobile:
   - menu hamburguesa
   - hero con foto
   - formulario de briefing
2. Proyectos:
   - /projects
   - /proyectos/iahorra-certus
   - /proyectos/academic-performance-prediction
   - /proyectos/customer-experience-loyalty-dashboard
   - /proyectos/automatizacion-reportes-mibanco
3. Recursos criticos:
   - CV descarga
   - imagenes AVIF/WebP
   - Open Graph en projects y fichas

## Si falla

1. Revert rapido:
   - git revert <commit_hash>
   - git push origin main
