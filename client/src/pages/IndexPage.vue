<template>
  <q-page class="">
    <q-spinner v-if="loading" />
    <div class="row">
      <HighlightCard :value="projectsCount" description="Projects" />
      <HighlightCard :value="contractorsCount" description="Contractors" />
      <HighlightCard :value="expendituresAmount" description="Spent" />

    </div>
    <div class="">
      <ProjectsMap :projects="projects"/>
    </div>
  </q-page>
</template>


<script>

import axios from 'axios';
import HighlightCard from 'src/components/HighlightCard.vue';
import ProjectsMap from 'src/components/ProjectsMap.vue';

export default {
  data() {
    return {
      loading: true,
      projectsCount: '',
      projects: [],
      expendituresAmount: '',
      contractorsCount: ''
    };
  },
  created() {
    this.fetchData('projects');
    this.fetchData('expenditures');
    this.fetchData('contractors');

  },
  components: {
    HighlightCard, 
    ProjectsMap
  },
  methods: {
    async fetchData(endpoint) {
      try {
        const response = await axios.get(`http://localhost:8000/api/${endpoint}`);
        const data = response.data
        switch (endpoint) {
          case 'projects':
            this.projectsCount = data.length;
            this.projects = data;
            break;
          case 'expenditures':
            const expenses = data.map(item => item.amount)
            this.expendituresAmount = "$"+ expenses.reduce(
              (accumulator, currentValue) => accumulator + currentValue,
              0,
            );
            break;
          case 'contractors':
            this.contractorsCount = data.length;
            break;
          default:
            console.log(`endpint ${endpoint} is not implemented`)
        }
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
