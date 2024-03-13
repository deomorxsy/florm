<template>
<div>
  <div class="container">
    <Bar v-if="loaded" :data="chartData" />
  </div>
</div>
</template>

<script>
// Import Chart.js and its components
import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js';
import { Bar } from 'vue-chartjs';

// Import the Sidebar component
import Sidebar from './SideBar.vue';

// Register Chart.js components
ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale);

export default {
  name: 'LineChart',
  components: {
    Sidebar, // Register the Sidebar component
    Bar, // Register the Bar component from vue-chartjs
  },
    data: () => ({
        loaded: false,
        chartData: null
    }),
    async mounted() {
        this.loaded = false
        const path = 'localhost:5000/alumni/2'

        try {
            const { userlist } = await axios.get(path)
                .then((res) => {
                    this.chartData = res.data;
                })
                .catch((error) => {
                    console.error(error)
                })
            this.chartData = userlist

            this.loaded = true
        } catch (e) {
            console.error(e)
        }
    }
}
</script>

<style>
/* Add your main app styling here */
body {
  margin: 0;
  font-family: 'Avenir', Helvetica, Arial, sans-serif;
  overflow:auto;

}

/* Add any additional styling for your main app */
</style>

