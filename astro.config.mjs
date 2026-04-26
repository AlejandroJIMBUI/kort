// @ts-check
import { defineConfig } from 'astro/config';

// https://astro.build/config
export default defineConfig({
  output: "static", // <-- generate static files
  base: "./",  // <-- relative base path for file:// URLs
  build: {
    assetsPrefix: "./", // <-- force relative paths in assets
  },
  vite: {
    build: {
      assetsDir: "assets",
    }
  }
});