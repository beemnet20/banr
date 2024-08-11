<template>
  <q-page class="q-pa-md">


    <div class="text-h6">Projects</div>



    <GenericTable apiEndpoint="projects" :columns="tableColumns" />

  </q-page>
</template>

<script>
import GenericTable from 'src/components/GenericTable.vue';

export default {
  components: {
    GenericTable
  },
  data() {
    return {
      // Example columns configuration
      tableColumns: [
        { name: 'id', label: 'ID', align: 'left' },
        { name: 'project_name', label: 'project name'},
        { name: 'city', label: 'city'},
        { name: 'state', label: 'state'},
        { name: 'project_status', label: 'project status'},
        { name: 'project_phase', label: 'project phase'}
      ]
    }
  }
}
</script>

<style scoped>
/* Optional styling */
.q-page {
  max-width: 100%;
}
</style>