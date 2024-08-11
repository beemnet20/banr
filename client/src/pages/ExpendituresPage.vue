<template>
  <q-page class="q-pa-md">


    <div class="text-h6">Expenditures</div>



    <GenericTable apiEndpoint="expenditures" :columns="tableColumns" />

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
        { name: 'expense_name', label: 'expense' },
        { name: 'amount', label: 'amount' },
        { name: 'date_incurred', label: 'date'},
        { name: 'description', label: 'description'},
        { name: 'category', label: 'category'},
        { name: 'project', label: 'project'}

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