import en from './i18n/locales/en.json'
import kz from './i18n/locales/kz.json'
import ru from './i18n/locales/ru.json'

//@ts-ignore
export default defineI18nConfig(() => {
    return {
        legacy: false,
        fallbackLocale: 'ru',
        messages: {ru,en,kz}
    }
  })
  