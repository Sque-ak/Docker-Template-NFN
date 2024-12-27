// https://nuxt.com/docs/api/configuration/nuxt-config
import { defineNuxtConfig } from 'nuxt/config'

export default defineNuxtConfig({
  compatibilityDate: '2024-11-01',

  devtools: { enabled: true },
  modules: ['nuxt-translation-manager', '@nuxtjs/i18n'],

  vite: {
      server: {
        hmr: {
        protocol: "http",
        host: 'localhost',
        clientPort: 3000,
        port: 3000,
      },
    },
  },

  'translation-manager': {
    langDir: 'i18n/locales'
  },
  i18n: {
    locales:[
      { code: 'en', iso: 'en-US', file: 'en.json' },
      { code: 'ru', iso: 'ru-RU', file: 'ru.json' },
      { code: 'kz', iso: 'kk-KZ', file: 'kz.json' },
    ],
    defaultLocale: 'ru',
    lazy: true,
    compilation: {
      strictMessage: false
    }
  },

})