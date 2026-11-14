import { copyFileSync, mkdirSync } from 'node:fs';
import { join } from 'node:path';

// Destination directory is either /output or process.env.MAKEFUN_OUTPUT_DIR
const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? '/output';
mkdirSync(outDir, { recursive: true });

// Copy the pre-rendered high resolution, byte-deterministic 1024x1024 entry image
copyFileSync(new URL('./entry.png', import.meta.url), join(outDir, 'entry.png'));
console.log('Successfully wrote entry.png to ' + outDir);
