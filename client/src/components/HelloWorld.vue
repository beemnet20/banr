<template>
  <q-page padding>
    <q-card>
      <q-card-section>
      </q-card-section>

      <q-card-section>
        <q-spinner v-if="loading" />
        <div v-else>{{ message }}</div>
      </q-card-section>
    </q-card>
  </q-page>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      message: '',
      loading: true,
    };
  },
  created() {
    this.fetchData();
  },
  methods: {
    async fetchData() {
      try {
        const response = await axios.get('http://localhost:8000/api/hello-world'); // Replace with your actual API endpoint
        this.message = response.data.message;
      } catch (error) {
        console.error('Error fetching data:', error);
        this.message = 'Error fetching data';
      } finally {
        this.loading = false;
      }
    },
  },
};
</script>

<style scoped>
</style>
