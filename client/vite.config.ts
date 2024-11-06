/// <reference types="vitest" />
import { fileURLToPath, URL } from "node:url"

import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"

// https://vite.dev/config/
export default defineConfig({
    plugins: [vue()],
    server: {
        host: "0.0.0.0"
    },
    resolve: {
        alias: {
            "@": fileURLToPath(new URL("./src", import.meta.url))
        }
    },
    test: {
        environment: "jsdom",
        setupFiles: ["./vitest.setup.ts"]
    }
})
