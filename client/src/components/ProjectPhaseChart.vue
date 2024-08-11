<template>
    <q-card class="q-ma-md">
        <q-card-section>
            <div class="text-h6">Project phases</div>
        </q-card-section>
        <q-card-section class="chart-section">
            <div class="chart-container">
                <apexchart type="bar" :options="chartOptions" :series="chartSeries"></apexchart>
            </div>
        </q-card-section>
    </q-card>
</template>

<script>
import VueApexCharts from 'vue3-apexcharts';

export default {
    components: {
        apexchart: VueApexCharts,
    },
    props: {
        projects: {
            type: Array,
            required: true,
        },
    },
    data() {
        return {
            chartOptions: {
                chart: {
                    id: 'project-phase-chart',
                    toolbar: {
                        show: false
                    }
                },
                xaxis: {
                    categories: [],
                },
                yaxis: {
                    title: {
                        text: 'Number of Projects'
                    }
                },
                plotOptions: {
                    bar: {
                        distributed: true,
                        horizontal: false,
                    }
                },
                dataLabels: {
                    enabled: false,
                }
            },
            chartSeries: [],
        };
    },
    watch: {
        projects: {
            handler(newVal) {
                this.updateChart(newVal);
            },
            immediate: true,
        },
    },
    methods: {
        updateChart(projects) {
            // Group projects by phase
            const phases = {};
            projects.forEach((project) => {
                const phase = project.project_phase;
                if (!phases[phase]) {
                    phases[phase] = 0;
                }
                phases[phase] += 1;
            });

            // Prepare data for the chart
            this.chartOptions.xaxis.categories = Object.keys(phases);
            this.chartSeries = [{
                name: 'Projects',
                data: Object.values(phases),
            }];
        },
    },
};
</script>

<style scoped>
.chart-container {
    height: 100%;
    width: 100%;
    min-height: 400px;
}

.chart-section{
    display: flex;
    flex-direction: column;
    justify-content: center;
    height: 100%;
    padding: 0
}
</style>