// news-image-20261118 entry point
// Hand-written deliverable: publish the prepared artwork as-is.
// The picture itself is produced ahead of time (see draw.py); this
// script only carries entry.png from the repo folder into whatever
// output directory the runner points us at.

import { readFileSync, writeFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const here = dirname(fileURLToPath(import.meta.url));
const sourcePath = join(here, "entry.png");

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const destPath = join(outDir, "entry.png");

const payload = readFileSync(sourcePath);
if (payload.byteLength === 0) {
  throw new Error(`refusing to publish an empty file: ${sourcePath}`);
}
writeFileSync(destPath, payload);

console.log(`published ${payload.byteLength} bytes -> ${destPath}`);
