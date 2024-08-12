<template>
    <div>

  
      <div>
        <q-table
          :rows="data"
          :columns="columns"
          row-key="id" 
          :pagination="pagination"
          :loading="loading"
        >
          <template v-slot:body="props">
            <q-tr :props="props">
              <q-td v-for="col in columns" :key="col.name" :props="props">
                <span v-if="col.name === 'id'">
                  <a :href="'/'+apiEndpoint+'/'+props.row[col.name]">{{ props.row[col.name] }}</a>
                </span>
                <span v-if="col.name !='id' ">
                  {{ props.row[col.name] }}
                </span>
               
              </q-td>
            </q-tr>
          </template>
        </q-table>
    </div>
    </div>
  </template>
  
  <script>
  import axios from 'axios';
  
  export default {
    props: {
      // The URL from which to fetch data
      apiEndpoint: {
        type: String,
        required: true
      },
      // The columns configuration for the table
      columns: {
        type: Array,
        required: true
      }
    },
    data() {
      return {
        // Data to be displayed in the table
        data: [],
        // Pagination settings for the table
        pagination: {
          rowsPerPage: 10
        },
        // Loading state for the table
        loading: true
      }
    },
    async mounted() {
      try {
        // Fetch data from the provided endpoint
        const response = await axios.get(`http://localhost:8000/api/${this.apiEndpoint}`);
        this.data = response.data;
      } catch (error) {
        console.error('Error fetching data:', error);
      } finally {
        this.loading = false;
      }
    }
  }
  </script>
  
  <style scoped>
  .q-card {
    max-width: 100%;
  }
  </style>
  