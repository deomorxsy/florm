<template>
</template>

<script>
import { Line } from 'vue-chartjs';
import axios from 'axios';

export default {
  extends: Line,
  data() {
    return {
      userId: 'your_user_id_here', // specify the user id you want to search for
      data: {
        labels: [],
        datasets: [
          {
            label: 'Data',
            backgroundColor: 'rgba(75, 192, 192, 0.2)',
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1,
            data: [],
          },
        ],
      },
    };
  },
  mounted() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get(`/your_endpoint/${this.userId}`);
        this.data.labels = response.data.labels;
        this.data.datasets[0].data = response.data.data;
        this.renderChart(this.data);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },
  },
};
</script>

