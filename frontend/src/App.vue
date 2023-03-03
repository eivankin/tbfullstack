<template>
  <main class="container-fluid">
    <div class="row">
      <div class="col-4">
        <tabs
          nav-class="nav nav-tabs"
          nav-item-class="nav-item"
          nav-item-link-class="nav-link"
          nav-item-link-active-class="nav-link active"
          id="tabs"
        >
          <tab name="Поиск" class="nav-item">
            <FilterForm ref="form" :onSubmit="onFilterSubmit" />
          </tab>
          <tab name="Статистика"> </tab>
        </tabs>
      </div>
      <div class="col-8" style="padding-right: 0">
        <MapWidget ref="map" />
      </div>
    </div>
  </main>
</template>
<script lang="ts">
import MapWidget from '@/components/MapWidget.vue'
import FilterForm from '@/components/FilterForm.vue'
import { defineComponent } from 'vue'
import type { FormRef, MapRef } from '@/types'

export default defineComponent({
  components: { MapWidget, FilterForm },
  methods: {
    onFilterSubmit(e: Event) {
      e.preventDefault()
      let formObj = this.$refs.form as FormRef
      let mapObj = this.$refs.map as MapRef
      mapObj.getSportObjects(
        formObj.fedEntity ? formObj.fedEntity.id : undefined,
        formObj.district ? formObj.district.id : undefined,
        formObj.locality ? formObj.locality.id : undefined,
        formObj.sportType ? formObj.sportType.id : undefined,
        formObj.sportObjectType ? formObj.sportObjectType.id : undefined
      )
    }
  }
})
</script>

<style scoped>
#tabs {
  margin-top: 0.5em;
}
</style>
