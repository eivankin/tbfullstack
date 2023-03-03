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
import type { ChartData } from 'chart.js'

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
    sportTypesData: Object as PropType<number[]>,
    sportTypesLabels: Object as PropType<string[]>,
    sportTypesColors: Object as PropType<string[]>,
    isLoaded: Boolean
  },
  computed: {
    sportTypesChartData(): ChartData<'pie'> {
      return {
        labels: this.sportTypesLabels,
        datasets: [
          {
            label: 'Количество объектов по видам спорта',
            data: this.sportTypesData ?? [],
            backgroundColor: this.sportTypesColors ?? []
          }
        ]
      }
    }
  }
})
</script>

<style scoped></style>
