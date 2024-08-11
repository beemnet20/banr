<template>
    <q-page class="q-pa-md">
  
  
      <div class="text-h6">Contractors</div>
  
  
  
      <GenericTable apiUrl="http://localhost:8000/api/contractors" :columns="tableColumns" />
  
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
          { name: 'company_name', label: 'company'},
          { name: 'field_of_work', label: 'field of work'},
          { name: 'contact_person', label: 'contact person'},
          { name: 'phone_number', label: 'phone number'},
          { name: 'email', label: 'email'}
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