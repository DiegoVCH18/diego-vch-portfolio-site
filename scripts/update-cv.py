from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_PDF = ROOT / "assets" / "CV_Diego_Vasquez.pdf"


LATEX = r"""
\documentclass[10pt,a4paper]{article}
\usepackage[margin=1.45cm]{geometry}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage[spanish]{babel}
\usepackage{xcolor}
\usepackage{tabularx}
\usepackage{enumitem}
\usepackage{hyperref}
\usepackage{titlesec}
\usepackage{array}
\usepackage{setspace}

\definecolor{accent}{HTML}{1F4E79}
\definecolor{textgray}{HTML}{444444}

\hypersetup{
  colorlinks=true,
  urlcolor=accent,
  linkcolor=accent,
  pdftitle={Diego Armando Vasquez Chavez - CV},
  pdfauthor={Diego Armando Vasquez Chavez}
}
\urlstyle{same}

\setlength{\parindent}{0pt}
\setlength{\parskip}{0.2em}
\setlength{\tabcolsep}{0pt}
\setstretch{1.0}
\raggedright
\sloppy

\titleformat{\section}{\large\bfseries\color{accent}}{}{0pt}{}[\vspace{0.15em}\titlerule]
\titlespacing*{\section}{0pt}{0.55em}{0.35em}
\setlist[itemize]{leftmargin=1.2em,itemsep=0.18em,topsep=0.18em}

\newcommand{\cvrole}[2]{\textbf{#1} \hfill {\small #2}\par}
\newcommand{\cvtitle}[1]{\textit{#1}\par}
\newcommand{\cvsmall}[1]{{\small #1}\par}

\begin{document}

{\Huge\bfseries Diego Armando Vasquez Chavez\par}
{\large Consultor de Datos, Business Intelligence y Desarrollo Web Full Stack\par}
\vspace{0.35em}
{\small Arequipa, Peru \textbar{} \href{mailto:diegovch@gmail.com}{diegovch@gmail.com} \textbar{} +51 974-205217 \textbar{} \href{https://www.linkedin.com/in/diego-armando-vasquez}{LinkedIn} \textbar{} \href{https://github.com/DiegoVCH18}{GitHub}}

\section*{Perfil}
Consultor orientado a resultados que convierte procesos manuales en soluciones digitales que ahorran tiempo, reducen errores y mejoran la toma de decisiones. Combino Business Intelligence, automatizaci\'on y desarrollo web a medida para entregar productos claros, escalables y listos para operar.

\section*{Servicios de consultor\'ia}
\begin{itemize}
  \item \textbf{Business Intelligence:} tableros ejecutivos, KPIs y seguimiento de gesti\'on para direcciones y equipos operativos.
  \item \textbf{Automatizaci\'on de reportes:} flujos con Excel, Power Query, VBA y Apps Script para bajar tiempos de consolidaci\'on y error manual.
  \item \textbf{Desarrollo Web Full Stack:} aplicaciones web, PWA y portales internos con frontend, l\'ogica de negocio, persistencia y despliegue en Vercel.
\end{itemize}

\section*{Competencias clave}
\begin{tabularx}{\textwidth}{@{}>{\bfseries}p{3.4cm}X@{}}
Business Intelligence & Power BI Desktop/Service, DAX, Power Query, modelado relacional y dimensional, data storytelling \\
Datos y ETL & SQL / MySQL, Microsoft 365, limpieza y transformaci\'on de datos, bases relacionales, control y trazabilidad \\
Desarrollo Web & React, Next.js, TypeScript, Firebase, Vercel, interfaces orientadas a producto \\
Automatizaci\'on & Excel VBA, Apps Script, macros, reportes autom\'aticos, integraci\'on con hojas de c\'alculo \\
Anal\'itica & Python, pandas, scikit-learn, XGBoost, CatBoost, Hugging Face, EDA y modelado predictivo \\
\end{tabularx}

\section*{Experiencia relevante}
\cvrole{Asociaci\'on UNACEM}{Mar. 2026 -- Oct. 2026}
\cvtitle{Consultor en Gesti\'on y An\'alisis de Data -- Laboratorio Social}
\begin{itemize}
  \item Desarrollo y ajuste de dashboards en Power BI para el seguimiento de proyectos sociales y reportes ejecutivos.
  \item ETL y modelado de bases de datos para trazabilidad de indicadores, filtros din\'amicos y control de calidad de datos.
  \item Generaci\'on de reportes estad\'isticos y soporte en confidencialidad, acceso y resguardo de informaci\'on institucional.
\end{itemize}

\cvrole{CERTUS}{Mar. 2021 -- Presente}
\cvtitle{Docente Innovador \& EdFinTech Developer | Carrera Administraci\'on Financiera y Banca Digital}
\begin{itemize}
  \item Creaci\'on de IAhorra CERTUS como propuesta de innovaci\'on educativa, con versi\'on web en React / Next.js y despliegue en Vercel.
  \item Desarrollo del Simulador SIAF y del M\'odulo Evaluador MYPE en Excel/VBA para competencias pr\'acticas en banca y finanzas.
  \item Dise\~no de recursos acad\'emicos con Fintech e IA, adem\'as de soporte a coordinaci\'on con tableros de KPI en Power BI.
\end{itemize}

\cvrole{MIBANCO -- Escuela de Negocios / Escuela de Formaci\'on}{Jun. 2025 -- Jul. 2025 / Ago. -- Sept. 2024 / Sept. 2023 -- Ene. 2024}
\cvtitle{Consultor Especializado en Automatizaci\'on, Datos y Evaluaci\'on de Competencias}
\begin{itemize}
  \item Dise\~no e implementaci\'on de un sistema automatizado con Power Query y VBA, reduciendo m\'as del 60\% el tiempo de consolidaci\'on mensual.
  \item Desarrollo de dashboards de KPIs para visualizaci\'on estrat\'egica por facilitador, agencia y programa.
  \item Construcci\'on de plantillas automatizadas para evaluaci\'on de casos, mapas de carrera y conexi\'on con Google Sheets mediante Apps Script.
\end{itemize}

\cvrole{PROAVANCE}{Abr. -- May. 2025 / Jul. 2025}
\cvtitle{Docente Especialista en Power BI | Instructor en Data Analytics}
\begin{itemize}
  \item Dise\~no y dictado del programa de capacitaci\'on Power BI para colaboradores de Sociedad Minera Cerro Verde.
  \item Elaboraci\'on de cursos e-learning de Tableau Public y Data Governance para profesionales del sector p\'ublico y privado.
\end{itemize}

\cvrole{TECZONE AQP}{Ene. 2015 -- Mar. 2024}
\cvtitle{Fundador | Consultor y Formador en Data Analytics \& Power BI}
\begin{itemize}
  \item Liderazgo de programas avanzados de capacitaci\'on en Power BI, Excel VBA y automatizaci\'on de procesos.
  \item Desarrollo de simuladores acad\'emicos y herramientas de an\'alisis personalizadas para organizaciones educativas y empresariales.
\end{itemize}

\section*{Proyectos seleccionados}
\begin{itemize}
  \item \textbf{IAhorra CERTUS -- Asistente Web de Educaci\'on Financiera:} app web con React / Next.js, Firebase, Gemini AI y despliegue en Vercel.
  \item \textbf{M\'odulo Evaluador MYPE:} soluci\'on web multi-rol con autenticaci\'on, scoring y exportaci\'on de reportes en PDF.
  \item \textbf{Simulador SIAF PWA:} producto web/PWA para formaci\'on pr\'actica en banca y finanzas con flujos operativos guiados.
  \item \textbf{Academic Performance Prediction:} modelo predictivo en Hugging Face para detectar riesgo acad\'emico con m\'as del 90\% de precisi\'on.
  \item \textbf{Customer Experience \& Loyalty Dashboard:} dashboard ejecutivo con CSAT, NPS y an\'alisis de churn orientado a gerencia.
\end{itemize}

\section*{Educaci\'on y certificaciones}
\begin{itemize}
  \item \textbf{Universidad Nacional de San Agust\'in (UNSA):} Ingeniero Industrial, colegiado CIP. MBA en Gerencia de Marketing y Ventas en curso.
  \item \textbf{Toulouse Lautrec:} Data Science \& Machine Learning.
  \item \textbf{Guayerd \& IBM SkillsBuild:} Data Analytics \& Fundamentos de IA.
\end{itemize}

\section*{Idiomas}
Espa\~nol: nativo \textbar{} Ingl\'es: intermedio, lectura t\'ecnica

\vspace{0.35em}
{\small \textcolor{textgray}{Consultor de datos y desarrollo digital enfocado en negocio, adopci\'on y resultados medibles.}}

\end{document}
"""


def build_pdf() -> None:
    work_dir = Path(tempfile.mkdtemp(prefix="cv-build-", dir=ROOT))
    try:
        tex_path = work_dir / "cv.tex"
        tex_path.write_text(LATEX, encoding="utf-8")

        command = [
            "pdflatex",
            "-interaction=nonstopmode",
            "-halt-on-error",
            "-output-directory",
            str(work_dir),
            str(tex_path),
        ]
        result = subprocess.run(command, capture_output=True, text=True)
        if result.returncode != 0:
            sys.stderr.write(result.stdout)
            sys.stderr.write(result.stderr)
            raise RuntimeError("Failed to build CV PDF")

        generated_pdf = work_dir / "cv.pdf"
        if not generated_pdf.exists():
            raise FileNotFoundError("Generated PDF not found")

        shutil.copy2(generated_pdf, OUTPUT_PDF)
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)


if __name__ == "__main__":
    build_pdf()
