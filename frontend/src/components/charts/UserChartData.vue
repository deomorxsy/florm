<template>
  <div>
    <h2>Chart for {{ selectedRow.nome }}</h2>
    <Scatter :data="data" :options="options" />
  </div>
</template>

<script lang="ts">
import {
  Chart as ChartJS,
  LinearScale,
  PointElement,
  LineElement,
  Tooltip,
  Legend
} from 'chart.js'
import { Scatter, Line } from 'vue-chartjs'
import * as chartConfig from './chartConfig.js'

ChartJS.register(LinearScale, PointElement, LineElement, Tooltip, Legend)

export default {
  name: 'App',
  components: {
    Scatter,
    Line
  },
  props: {
    selectedRow: Object
  },
  data() {
    return chartConfig
  }
};
</script>

