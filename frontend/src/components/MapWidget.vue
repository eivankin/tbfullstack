<template>
  <div
    class="d-flex justify-content-center align-items-center"
    id="main-spinner"
    :style="isLoaded ? 'display: none !important' : ''"
  >
    <Spinner style="width: 5em; height: 5em" />
  </div>
  <mapbox-map
    :access-token="accessToken"
    height="100vh"
    :style="isLoaded ? '' : 'display: none !important'"
    @loaded="isLoaded = true"
    auto-resize="auto-resize"
    :center="[94, 60]"
    :zoom="3"
  >
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
</template>
<script lang="ts">
import axios from 'axios'
import { defineComponent } from 'vue'
import Spinner from '@/components/Spinner.vue'
import type { SportObject, SportObjectInfo } from '@/types'

export default defineComponent({
  components: { Spinner },

  data(): { name: string; accessToken: string; sportObjects: SportObject[]; isLoaded: boolean } {
    return {
      name: 'MapWidget',
      accessToken: import.meta.env.VITE_MAPBOX_API_KEY,
      sportObjects: [],
      isLoaded: false
    }
  },
  expose: ['getSportObjects'],
  methods: {
    getSportObjects(
      fedEntityId: number | undefined = undefined,
      districtId: number | undefined = undefined,
      localityId: number | undefined = undefined,
      sportTypeId: number | undefined = undefined,
      sportObjectTypeId: number | undefined = undefined
    ) {
      axios
        .get(
          `${import.meta.env.VITE_API_ENDPOINT}/sport-objects/?${
            fedEntityId ? `fed_entity_id=${fedEntityId}` : ''
          }&${districtId ? `district_id=${districtId}` : ''}&${
            localityId ? `locality_id=${localityId}` : ''
          }&${sportTypeId ? `sport_type_id=${sportTypeId}` : ``}&${
            sportObjectTypeId ? `sport_object_type_id=${sportObjectTypeId}` : ''
          }`
        )
        .then((response) => {
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

<style scoped>
#main-spinner {
  height: 100vh;
}
</style>
