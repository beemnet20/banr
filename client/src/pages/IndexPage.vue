<template>
  <q-page class="">
    <q-spinner v-if="loading" />
    <div class="row q-ma-sm">
      <HighlightCard :value="activeProjectsCount" description=" active projects" />
      <HighlightCard :value="completedProjectsCount" description=" completed projects" />
      <HighlightCard :value="contractorsCount" description=" contractors" />
      <HighlightCard prefix="$" :value="expendituresAmount" description=" spent" />

    </div>
    <div v-if="projects.length > 0" class="row">
      <div class="col-12 col-md-8">
        <ProjectsMap :projects="projects" />
      </div>
      <div class="col-12 col-md-4">
        <ProjectPhaseChart :projects="projects" />
      </div>

    </div>
  </q-page>
</template>


<script>

import axios from 'axios';
import HighlightCard from 'src/components/HighlightCard.vue';
import ProjectPhaseChart from 'src/components/ProjectPhaseChart.vue';
import ProjectsMap from 'src/components/ProjectsMap.vue';

export default {
  data() {
    return {
      loading: true,
      activeProjectsCount: 0,
      completedProjectsCount: 0,
      projects: [],
      expendituresAmount: 0,
      contractorsCount: 0
    };
  },
  created() {
    this.fetchData('projects');
    this.fetchData('expenditures');
    this.fetchData('contractors');

  },
  components: {
    HighlightCard,
    ProjectsMap,
    ProjectPhaseChart
  },
  methods: {
    async fetchData(endpoint) {
      try {
        const response = await axios.get(`http://localhost:8000/api/${endpoint}`);
        const data = response.data
        switch (endpoint) {
          case 'projects':
            this.activeProjectsCount = data.filter(project => project.project_status === 'active').length;
            this.completedProjectsCount = data.filter(project => project.project_status === 'completed').length;
            this.projects = data;
            break;
          case 'expenditures':
            const expenses = data.map(item => item.amount)
            this.expendituresAmount = expenses.reduce(
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
