<template>
  <div class="container-fluid chart-container">
    <IsLoaded :is-loaded="isLoaded" />
    <Pie
      :options="chartOptions"
      :data="sportTypesChartData"
      :style="isLoaded ? '' : 'display: none !important'"
    />
  </div>
</template>

<script lang="ts">
import { Pie } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  ArcElement
} from 'chart.js'
import { defineComponent } from 'vue'
import type { PropType } from 'vue'
import IsLoaded from '@/components/IsLoaded.vue'

ChartJS.register(Title, Tooltip, Legend, CategoryScale, LinearScale, ArcElement)

export default defineComponent({
  name: 'SportTypesChart',
  components: { IsLoaded, Pie },
  data() {
    return {
      chartOptions: {
        responsive: true
      }
    }
  },
  props: {
    sportTypesData: Object as PropType<Array<Number>>,
    sportTypesLabels: Object as PropType<Array<String>>,
    sportTypesColors: Object as PropType<Array<String>>,
    isLoaded: Boolean
  },
  computed: {
    sportTypesChartData() {
      return {
        labels: this.sportTypesLabels,
        datasets: [
          {
            label: 'Количество объектов по видам спорта',
            data: this.sportTypesData,
            backgroundColor: this.sportTypesColors
          }
        ]
      }
    }
  }
})
</script>

<style scoped></style>
