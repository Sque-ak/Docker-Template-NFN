<script setup>
const { setLocale } = useI18n()
</script>

<template>
  <div>
    <div>
      <button @click="setLocale('en')">en</button>
      <button @click="setLocale('ru')">ru</button>
      <button @click="setLocale('kz')">kz</button>
      <p>{{ $t('welcome') }}</p>
      <NuxtPage />
    </div>
  </div>
</template>