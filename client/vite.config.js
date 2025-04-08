import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,  // Ensure the frontend runs on 5173
    proxy: {
      "/api": {
        target: "http://localhost:5000",  // Proxy API requests to backend
        changeOrigin: true,
        secure: false,
      },
    },
  },
});
