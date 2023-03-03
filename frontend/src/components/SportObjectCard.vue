<script setup lang="ts">
import { ref, defineExpose } from 'vue'
import type { SportObjectInfo } from '@/types'
import type { Ref } from 'vue'

const sportObject: Ref<SportObjectInfo> = ref({
  name: null,
  short_description: null,
  full_description: null,
  address: null
})

defineExpose({ sportObject })
</script>
<template>
  <table class="table">
    <tbody>
      <tr>
        <th scope="row">Название</th>
        <td>{{ sportObject.name ?? 'Нет данных' }}</td>
      </tr>
      <tr>
        <th scope="row">Краткое описание</th>
        <td>{{ sportObject.short_description ?? 'Нет данных' }}</td>
      </tr>
      <tr>
        <th scope="row">Детальное описание</th>
        <td>{{ sportObject.full_description ?? 'Нет данных' }}</td>
      </tr>
      <tr>
        <th scope="row">Адрес</th>
        <td>{{ sportObject.address ?? 'Нет данных' }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script lang="ts">
import { defineComponent } from 'vue'

export default defineComponent({
  name: 'SportObjectCard'
})
</script>

<style scoped></style>
