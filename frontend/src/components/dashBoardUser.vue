<template>
  <div>
    <!-- Import and use the Sidebar component -->
    <Sidebar />

    <!-- Your main content goes here -->
    <router-view />
  </div>
      <div>
    <!-- Header -->
    <header>
      <h1>User Dashboard</h1>
    </header>
    <!-- Main Content -->
    <main>
      <section>
        <h2>Welcome, {{ username }}!</h2>
        <!-- Add your dashboard content here -->
      </section>
    </main>

    <div class="container mt-3">
      <div class="row">
        <div class="col-md-8">
          <div class="card">
            <div class="card-body">
              <Bar
                id="my-chart-id1"
                :options="chartOptions"
                :data="chartData1"
              />
            </div>
          </div>
         <div class="card">
            <div class="card-body">
              <Bar
                id="my-chart-id2"
                :options="chartOptions"
                :data="chartData2"
              />
            </div>
          </div>
         <div class="card">
            <div class="card-body">
              <Bar
                id="my-chart-id2"
                :options="chartOptions"
                :data="chartData3"
              />
            </div>
          </div>
        </div>
        <div class="col-md-4">
          <!-- Other dashboard elements can be added here -->
        </div>
      </div>
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
  name: 'CombinedComponent',
  components: {
    Sidebar, // Register the Sidebar component
    Bar, // Register the Bar component from vue-chartjs
  },
  data() {
    return {
      chartData1: {
        labels: ['January', 'February', 'March'],
        datasets: [{ data: [40, 20, 12] }],
      },
      chartData2: {
        labels: ['April', 'May', 'June'],
        datasets: [{ data: [30, 25, 18] }],
      },
      chartData3: {
        labels: ['July', 'August', 'September'],
        datasets: [{ data: [35, 15, 22] }],
      },
      chartOptions: {
        responsive: true,
      },
    };
  },
};

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
