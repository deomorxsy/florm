<template>
  <div>
    <div class="table-container">
      <h1>User Data</h1>

      <div class="search-box">
        <input type="text" v-model="search" placeholder="Search by name">
      </div>

      <table>
        <thead>
          <tr>
            <th>ID</th>
            <th>Name</th>
            <th>CPF</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="user in paginatedUsers" :key="user.id" @click="toggleRow(user.id)">
            <td>{{ user.id }}</td>
            <td>{{ user.nome }}</td>
            <td>{{ user.cpf }}</td>
          </tr>
          <tr v-if="selectedRow">
            <td :colspan="columnCount">
              <div class="short-window">
                <!-- Your short window content goes here -->
                Short window content for {{ selectedRow.nome }}
                <UserChartData :selectedRow="selectedRow"/>
              </div>
            </td>
          </tr>
        </tbody>
      </table>
      <div class="pagination">
        <button @click="changePage(1)">«</button>
        <button v-for="pageNumber in visiblePageNumbers" :key="pageNumber" @click="changePage(pageNumber)">
          {{ pageNumber }}
        </button>
        <button @click="changePage(pageCount)">»</button>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios';
import UserChartData from './charts/UserChartData.vue'; // Import the chart component

export default {
  components: {
        UserChartData
    },
  data() {
    return {
      users: [],
      search: '',
      currentPage: 1,
      pageSize: 10,
      selectedRow: null,
      columnCount: 3 // Number of columns in your table
    };
  },
  mounted() {
    this.fetchUserData();
  },
  methods: {
    fetchUserData() {
      axios.get('http://localhost:5000/alumni/')
        .then(response => {
          this.users = response.data;
        })
        .catch(error => {
          console.error('Error fetching user data:', error);
        });
    },
    changePage(pageNumber) {
      this.currentPage = pageNumber;
    },
    toggleRow(rowId) {
      if (this.selectedRow === rowId) {
        this.selectedRow = null;
      } else {
        this.selectedRow = rowId;
      }
    }
  },
  computed: {
    filteredUsers() {
      return this.users.filter(user =>
        user.nome.toLowerCase().includes(this.search.toLowerCase())
      );
    },
    pageCount() {
      return Math.ceil(this.filteredUsers.length / this.pageSize);
    },
    visiblePageNumbers() {
      const totalVisiblePages = 5; // Change this to the desired number of visible page numbers
      const startPage = Math.max(1, this.currentPage - Math.floor(totalVisiblePages / 2));
      const endPage = Math.min(this.pageCount, startPage + totalVisiblePages - 1);
      const visiblePages = [];
      for (let i = startPage; i <= endPage; i++) {
        visiblePages.push(i);
      }
      return visiblePages;
    },
    paginatedUsers() {
      const startIndex = (this.currentPage - 1) * this.pageSize;
      return this.filteredUsers.slice(startIndex, startIndex + this.pageSize);
    }
  }
};
</script>

<style>
.table-container {
  margin: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
  border-spacing: 0;
}

th,
td {
  padding: 8px 12px;
  text-align: left;
  border-bottom: 1px solid #ccc;
  position: relative;
}

th {
  background-color: #f4f6f8;
}

tr:nth-child(even) {
  background-color: #f9fafb;
}

tr:hover {
  background-color: #f1f4f8;
}

.short-window {
  position: absolute;
  background-color: #fff;
  border: 1px solid #ccc;
  padding: 10px;
  top: calc(100% + 5px);
  left: 0;
  width: 100%;
  z-index: 999;
}
</style>

