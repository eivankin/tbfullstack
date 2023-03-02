<script setup lang="ts"></script>
import Spinner from './components/Spinner.vue'
<template>
  <main>
    <mapbox-map :access-token="accessToken" height="1000px">
      <mapbox-navigation-control />
      <mapbox-marker
        v-for="object in sportObjects"
        :lng-lat="[object.longitude, object.latitude]"
        :color="object.is_active ? 'green' : 'red'"
      >
        <mapbox-popup @open="loadData(object.id, $event)" :offset="[0, -30]">
          <Spinner />
        </mapbox-popup>
      </mapbox-marker>
    </mapbox-map>
  </main>
</template>
<script lang="ts">
import axios from 'axios'
import { defineComponent } from 'vue'
import Spinner from '@/components/Spinner.vue'

type SportObject = {
  id: number
  latitude: number
  longitude: number
  is_active: boolean
}

type SportObjectInfo = {
  name: string
}

export default defineComponent({
  components: { Spinner },

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
    },
    loadData(objectId: number, event: { target: { _content: HTMLElement } }) {
      let container = event.target._content
      axios
        .get(`${import.meta.env.VITE_API_ENDPOINT}/sport-objects/${objectId}`)
        .then((response: { data: SportObjectInfo }) => {
          container.innerHTML = response.data.name
        })
    }
  },
  mounted() {
    this.getSportObjects()
  }
})
</script>
