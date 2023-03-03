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
          <tab name="Поиск" id="search">
            <FilterForm ref="form" :onSubmit="onFilterSubmit" />
          </tab>
          <tab id="activity-stats" name="Статистика | Активность объектов">
            <ActivityChart :activity-data="activityData" :is-loaded="areStatisticsLoaded" />
          </tab>
          <tab id="sport-type-stats" name="Статистика | Виды спорта">
            <SportTypesChart
              :sport-types-data="sportTypesData"
              :sport-types-labels="sportTypesLabels"
              :sport-types-colors="sportTypesColors"
              :is-loaded="areStatisticsLoaded"
            />
          </tab>
        </tabs>
      </div>
      <div class="col-8" style="padding-right: 0">
        <MapWidget @stats-data-upd="statsDataUpd" ref="map" />
      </div>
    </div>
  </main>
</template>
<script lang="ts">
import MapWidget from '@/components/MapWidget.vue'
import FilterForm from '@/components/FilterForm.vue'
import ActivityChart from '@/components/ActivityChart.vue'
import { defineComponent } from 'vue'
import type { FormRef, MapRef } from '@/types'
import SportTypesChart from '@/components/SportTypesChart.vue'

export default defineComponent({
  components: { SportTypesChart, MapWidget, FilterForm, ActivityChart },
  data(): {
    activityData: number[]
    areStatisticsLoaded: boolean
    sportTypesData: number[]
    sportTypesLabels: string[]
    sportTypesColors: string[]
  } {
    return {
      activityData: [0, 0],
      sportTypesData: [],
      sportTypesLabels: [],
      areStatisticsLoaded: false,
      sportTypesColors: []
    }
  },
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
    },
    randomColor(): string {
      let r = Math.floor(Math.random() * 255)
      let g = Math.floor(Math.random() * 255)
      let b = Math.floor(Math.random() * 255)
      return 'rgb(' + r + ',' + g + ',' + b + ')'
    },
    randomColors(count: number): string[] {
      let result: string[] = Array(count)
      result.fill('')
      console.log(result.map(() => this.randomColor()))
      return result.map(() => this.randomColor())
    },
    statsDataUpd(activityData: number[], sportTypes: string[], sportTypesData: number[]) {
      this.activityData = activityData
      this.sportTypesData = sportTypesData
      this.sportTypesLabels = sportTypes
      this.sportTypesColors = this.randomColors(sportTypesData.length)
      this.areStatisticsLoaded = true
    }
  }
})
</script>

<style scoped>
#tabs {
  margin-top: 0.5em;
}
</style>
