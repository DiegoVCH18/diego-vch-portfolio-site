import { mkdir, readdir, readFile, rm, stat, writeFile, copyFile } from "node:fs/promises";
import { join, dirname } from "node:path";
import { minify } from "html-minifier-terser";

const root = process.cwd();
const distDir = join(root, "dist");

const htmlEntries = [
  "index.html",
  "projects.html",
  "proyectos/iahorra-certus.html",
  "proyectos/academic-performance-prediction.html",
  "proyectos/customer-experience-loyalty-dashboard.html",
  "proyectos/automatizacion-reportes-mibanco.html"
];

const minifyOptions = {
  collapseWhitespace: true,
  removeComments: true,
  removeRedundantAttributes: true,
  removeScriptTypeAttributes: true,
  removeStyleLinkTypeAttributes: true,
  minifyCSS: true,
  minifyJS: true
};

async function ensureDir(path) {
  await mkdir(path, { recursive: true });
}

async function copyDir(src, dest) {
  await ensureDir(dest);
  const entries = await readdir(src, { withFileTypes: true });
  for (const entry of entries) {
    const srcPath = join(src, entry.name);
    const destPath = join(dest, entry.name);
    if (entry.isDirectory()) {
      await copyDir(srcPath, destPath);
    } else {
      await copyFile(srcPath, destPath);
    }
  }
}

async function build() {
  await rm(distDir, { recursive: true, force: true });
  await ensureDir(distDir);

  for (const relPath of htmlEntries) {
    const srcPath = join(root, relPath);
    const srcStat = await stat(srcPath);
    if (!srcStat.isFile()) {
      throw new Error(`No se encontro archivo HTML: ${relPath}`);
    }

    const rawHtml = await readFile(srcPath, "utf8");
    const minifiedHtml = await minify(rawHtml, minifyOptions);

    const outPath = join(distDir, relPath);
    await ensureDir(dirname(outPath));
    await writeFile(outPath, minifiedHtml, "utf8");
  }

  await copyDir(join(root, "assets"), join(distDir, "assets"));
}

build().catch((error) => {
  console.error(error);
  process.exit(1);
});
