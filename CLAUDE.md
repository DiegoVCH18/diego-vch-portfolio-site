# CLAUDE.md — diego-vch-portfolio-site

## Qué es este proyecto
Portafolio profesional de Diego Armando Vasquez Chavez (Especialista en Gestión de Datos & BI, Power BI, Ing. Industrial). Sitio estático HTML/CSS/JS sin framework, desplegado en Vercel.
- Demo: https://diego-vch-portfolio-site.vercel.app
- GitHub: DiegoVCH18 · LinkedIn: diego-armando-vasquez

## Arquitectura
- `index.html` — homepage (hero, formulario de briefing, logos)
- `projects.html` — listado de proyectos
- `proyectos/*.html` — 8 fichas de detalle por proyecto (iahorra-certus, academic-performance-prediction, customer-experience-loyalty-dashboard, automatizacion-reportes-mibanco, minimarket-aurelion, modulo-evaluador-mype, simulador-siaf-comercial, xlsform-sgp-evaluacion-productores)
- `assets/` — imágenes (hero en .avif/.webp/.jpg), CV_Diego_Vasquez.pdf, logos, xlsform/
- `scripts/build-dist.mjs` — bundler propio: minifica HTML (html-minifier-terser) y copia assets a `dist/`
- `scripts/release.ps1` y `release-and-open.ps1` — flujo de release en PowerShell
- `vercel.json` — buildCommand `npm run build`, output `dist/`, cleanUrls

## Comandos
- `npm run build` — genera dist/ minificado
- `npm run release` — build + flujo de release completo (PowerShell)
- `npm run go` — release + abrir en navegador
- Entorno: Windows 11, Node 24, npm 11

## Reglas importantes
1. **Al crear una página nueva en `proyectos/`, agregarla SIEMPRE a `htmlEntries` en `scripts/build-dist.mjs`** — si no, no llega a producción.
2. Editar los HTML fuente en raíz/proyectos, NUNCA los de `dist/` (se regeneran en cada build).
3. Antes de release seguir `release-checklist.md`: validación visual local → npm run release → verificar dist/ → git diff → commit.
4. Imágenes hero: mantener los 3 formatos (.avif, .webp, .jpg) al reemplazar.
5. El CV enlazado es `assets/CV_Diego_Vasquez.pdf` — al actualizar CV, reemplazar ahí (existe `scripts/update-cv.py`).
6. Idioma del sitio y del contenido: español (Perú). Tono profesional de marca personal.

## Contexto de marca personal
El sitio es la pieza central de la marca "Diego VCH": consultor de datos con 10+ años en impacto social, educación y banca; 1.º lugar nacional Premio SBS 2025. Cualquier cambio de contenido debe reforzar ese posicionamiento.
