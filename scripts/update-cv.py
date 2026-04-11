from __future__ import annotations

import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from pypdf import PdfReader, PdfWriter


ROOT = Path(__file__).resolve().parents[1]
SOURCE_PDF = ROOT / "assets" / "CV_Diego_Vasquez.pdf"


def build_cover_pdf(work_dir: Path) -> Path:
    tex_path = work_dir / "cv-cover.tex"
    tex_path.write_text(
        r"""
\documentclass[11pt]{article}
\usepackage[margin=1.45cm]{geometry}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\pagestyle{empty}
\setlength{\parindent}{0pt}
\setlength{\parskip}{0.55em}
\begin{document}

{\Huge\bfseries Diego Armando Vasquez Chavez\par}
{\Large Consultor de Datos \& Business Intelligence \textbar{} Power BI \textbar{} Data Analytics \textbar{} Desarrollador Web Full Stack\par}

\vspace{0.4cm}

{\large Perfil comercial}\par
Transformo datos, procesos y necesidades de negocio en soluciones listas para operar. Combino gesti\'on y an\'alisis de datos en Microsoft 365, dashboards ejecutivos en Power BI, automatizaci\'on de reportes y desarrollo web para entregar productos claros, escalables y enfocados en resultados.

\vspace{0.2cm}

{\large Evidencia como Desarrollador Web Full Stack}\par
\begin{itemize}
  \item \textbf{IAhorra CERTUS}: app web con React, Next.js, Firebase, Gemini AI y despliegue en Vercel para educaci\'on financiera digital.
  \item \textbf{M\'odulo Evaluador MYPE}: soluci\'on web multi-rol con React, TypeScript, Firebase y exportaci\'on de reportes para evaluaci\'on crediticia.
  \item \textbf{Simulador SIAF PWA}: producto web/PWA para formaci\'on pr\'actica en banca y finanzas con flujos operativos guiados.
\end{itemize}

\vspace{0.1cm}

{\large Enfoque de trabajo}\par
Construyo experiencias web completas que ayudan a vender, operar y escalar: interfaz, l\'ogica de negocio, persistencia de datos, integraciones y despliegue.

\vfill

{\small Arequipa, Peru \textbar{} \texttt{diegovch@gmail.com} \textbar{} \texttt{+51 974-205217} \textbar{} \texttt{github.com/DiegoVCH18}}

\end{document}
""",
        encoding="utf-8",
    )

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
        raise RuntimeError("Failed to build CV cover PDF")
    return work_dir / "cv-cover.pdf"


def prepend_cover(source_pdf: Path, cover_pdf: Path) -> None:
    cover_reader = PdfReader(str(cover_pdf))
    source_reader = PdfReader(str(source_pdf))
    writer = PdfWriter()

    for page in cover_reader.pages:
        writer.add_page(page)
    for page in source_reader.pages:
        writer.add_page(page)

    if source_reader.metadata is not None:
        writer.add_metadata({k: v for k, v in source_reader.metadata.items() if v is not None})

    temp_output = source_pdf.with_suffix(".tmp.pdf")
    with temp_output.open("wb") as handle:
        writer.write(handle)
    temp_output.replace(source_pdf)


def main() -> None:
    if not SOURCE_PDF.exists():
        raise FileNotFoundError(f"Missing source PDF: {SOURCE_PDF}")

    work_dir = Path(tempfile.mkdtemp(prefix="cv-update-", dir=ROOT))
    try:
        cover_pdf = build_cover_pdf(work_dir)
        prepend_cover(SOURCE_PDF, cover_pdf)
    finally:
        shutil.rmtree(work_dir, ignore_errors=True)


if __name__ == "__main__":
    main()
