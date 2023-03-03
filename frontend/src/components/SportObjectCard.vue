<template>
  <table class="table">
    <tbody>
      <tr>
        <th scope="row">Название</th>
        <td>{{ sportObject.name }}</td>
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
        <td>{{ sportObject.address }}</td>
      </tr>
    </tbody>
  </table>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import type { SportObjectInfo } from '@/types'
import type { PropType } from 'vue'

export default defineComponent({
  name: 'SportObjectCard',
  props: {
    sportObject: Object as PropType<SportObjectInfo>
  }
})
</script>

<style scoped></style>
