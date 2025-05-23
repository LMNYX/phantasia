import tailwindcss from "@tailwindcss/vite";

// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
  css: [
    '@/assets/css/main.scss'
  ],
  app: {
    buildAssetsDir: '_assets',
    head: {
      title: "uwu.so",
      charset: 'utf-16',
      viewport: 'width=device-width, initial-scale=1, maximum-scale=1',
      meta: [
        { name: 'description', content: 'Heavily opinionated image and file server.' }
      ],
    }
  },
  compatibilityDate: '2025-05-15',
  devtools: { enabled: true },
  modules: [
    '@nuxt/image',
    '@nuxt/fonts',
    '@nuxt/icon',
    '@nuxt/scripts',
    'nuxt-charts'
  ],
  fonts:
  {
    defaults: {
      weights: [300, 400, 500, 600, 700, 800],
      styles: ['normal', 'italic']
    }
  }
})