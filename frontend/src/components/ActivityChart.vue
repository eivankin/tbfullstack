<template>
  <div class="container-fluid chart-container">
    <IsLoaded :is-loaded="isLoaded" />
    <Bar
      :options="chartOptions"
      :data="activityChartData"
      :style="isLoaded ? '' : 'display: none !important'"
    />
  </div>
</template>

<script lang="ts">
import { Bar } from 'vue-chartjs'
import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  BarElement,
  CategoryScale,
  LinearScale
} from 'chart.js'
import { defineComponent } from 'vue'
import type { PropType } from 'vue'
import IsLoaded from '@/components/IsLoaded.vue'

ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)

export default defineComponent({
  name: 'ActivityChart',
  components: { IsLoaded, Bar },
  data() {
    return {
      chartOptions: {
        responsive: true
      }
    }
  },
  props: {
    activityData: Object as PropType<Array<Number>>,
    isLoaded: Boolean
  },
  computed: {
    activityChartData() {
      return {
        labels: ['Активен', 'Не активен'],
        datasets: [
          {
            label: 'Статус спортивных объектов',
            data: this.activityData,
            backgroundColor: ['green', 'red']
          }
        ]
      }
    }
  }
})
</script>

<style scoped></style>
