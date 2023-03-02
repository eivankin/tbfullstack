<script setup lang="ts"></script>

<template>
  <main>
    <mapbox-map :access-token="accessToken" height="1000px">
      <mapbox-marker
        v-for="object in sportObjects"
        :lng-lat="[object.longitude, object.latitude]"
      />
    </mapbox-map>
  </main>
</template>
<script lang="ts">
import axios from 'axios'
import { defineComponent } from 'vue'

type SportObject = {
  latitude: number
  longitude: number
}

export default defineComponent({
  data(): { accessToken: string; sportObjects: SportObject[] } {
    return {
      accessToken: import.meta.env.VITE_MAPBOX_API_KEY,
      sportObjects: []
    }
  },
  methods: {
    getSportObjects() {
      axios.get(`${import.meta.env.VITE_API_ENDPOINT}/sport-objects/`).then((response) => {
        this.sportObjects = response.data
      })
    }
  },
  mounted() {
    this.getSportObjects()
  }
})
</script>
