<template>
  <div
    class="d-flex justify-content-center align-items-center is-loaded"
    :style="isLoaded ? 'display: none !important' : ''"
  >
    <Spinner style="width: 5em; height: 5em" />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue'
import Spinner from '@/components/Spinner.vue'

export default defineComponent({
  components: { Spinner },
  name: 'IsLoaded',
  props: {
    isLoaded: Boolean
  }
})
</script>

<style scoped>
.is-loaded {
  height: 100vh;
}
</style>
