<template>
    <q-page class="q-pa-md">
        <div class="text-h6 q-ma-md">
            {{ projectId ? `Project: ${project.project_name}` : 'Create New Project' }}
        </div>
        <div class="row">
            <div class="col-4">
                <HighlightCard prefix="$" :value="project.total_expenses" description=" spent" />
            </div>
        </div>

        <q-form @submit="onSubmit" class="q-gutter-md q-mt-md">
            <div class="row">
                <div class="col-12 col-md-6">
                    <q-input class="col-6 q-ma-sm" filled v-model="project.project_name" label="Project Name"
                        :disable="isLoading" />
                    <q-input class="q-ma-sm" filled v-model="project.city" label="City" :disable="isLoading" />
                    <q-select class="q-ma-sm" :options="usStateOptions" filled v-model="project.state" label="State"
                        :disable="isLoading" />
                    <q-input class="q-ma-sm" filled v-model="project.zipcode" label="ZIP Code" type="number"
                        :disable="isLoading" />
                    <q-select class="q-ma-sm" filled :options="projectStatusOptions" v-model="project.project_status"
                        label="Project Status" :disable="isLoading" />
                    <q-select class="q-ma-sm" filled :options="projectPhaseOptions" v-model="project.project_phase"
                        label="Project Phase" :disable="isLoading" />
                </div>
                <div class="col-12 col-md-6">
                    <div v-if="project.zipcode" class="q-ma-sm">
                        <ProjectBoundaries @update-boundaries="onUpdateBoundaries" :zipcode="project.zipcode"
                            :projectSiteBoundaries="project.project_site_boundaries" />
                    </div>
                </div>
            </div>
            <div class="row q-mt-none">
                <q-select class="col q-ma-sm" multiple filled v-model="project.contractors" label="Contractors"
                    :options="contractorOptions" option-value="id" option-label="company_name" emit-value map-options
                    :disable="isLoading || isContractorsLoading" />
                <q-input class="col q-ma-sm" type="number" v-model="project.power_rating_gw" filled label="Power Rating (GW)" :disable="isLoading"/>
                <q-input class="col q-ma-sm" type="number" v-model="project.budget" filled label="Budget ($)" :disable="isLoading"/>
            </div>
            <div class="row q-mt-none">
                <q-input filled class="col q-ma-sm" type="date" v-model="project.estimated_construction_start_date" label="Estimated Construction Start" :disable="isLoading"/>
                <q-input filled class="col q-ma-sm" type="date" v-model="project.construction_start_date" label="Construction Start" :disable="isLoading"/>
                <q-input filled class="col q-ma-sm" type="date" v-model="project.estimated_construction_completion_date" label="Estimated Construction Completion" :disable="isLoading"/>
                <q-input filled class="col q-ma-sm" type="date" v-model="project.construction_completion_date" label="Construction Completion" :disable="isLoading"/>
            </div>
            <div class="row q-mt-none">
                <q-input filled class="col q-ma-sm" type="textarea" v-model="project.notes" label="Notes" :disable="isLoading"/>
            </div>
            <div class="row">
                <q-btn v-if="projectId" type="button" class="col q-ma-sm"  label="Delete Project"  color="negative" @click="onDelete" :disable="isLoading" />
                <q-btn class="col q-ma-sm" type="submit" label="Save Project" color="primary" :disable="isLoading" />
            </div>
        </q-form>
    </q-page>
</template>

<script>
import axios from 'axios';
import { Notify } from 'quasar';
import HighlightCard from 'src/components/HighlightCard.vue';
import ProjectBoundaries from 'src/components/ProjectBoundaries.vue';

export default {
    components: {
        HighlightCard,
        ProjectBoundaries
    },
    setup() {
        return {
            projectStatusOptions: ['active', 'completed'],
            usStateOptions: [
                'Alabama', 'Alaska', 'Arizona', 'Arkansas', 'California', 'Colorado', 'Connecticut',
                'Delaware', 'Florida', 'Georgia', 'Hawaii', 'Idaho', 'Illinois', 'Indiana', 'Iowa', 'Kansas',
                'Kentucky', 'Louisiana', 'Maine', 'Maryland', 'Massachusetts', 'Michigan', 'Minnesota',
                'Mississippi', 'Missouri', 'Montana', 'Nebraska', 'Nevada', 'New Hampshire', 'New Jersey',
                'New Mexico', 'New York', 'North Carolina', 'North Dakota', 'Ohio', 'Oklahoma', 'Oregon',
                'Pennsylvania', 'Rhode Island', 'South Carolina', 'South Dakota', 'Tennessee', 'Texas', 'Utah',
                'Vermont', 'Virginia', 'Washington', 'West Virginia', 'Wisconsin', 'Wyoming'
            ],
            projectPhaseOptions: ['design', 'design review', 'design approval', 'construction', 'testing', 'regulatory review', 'operational']
        }
    },
    data() {
        return {
            project: {
                project_name: '',
                city: '',
                state: '',
                zipcode: '',
                project_status: null,
                project_phase: null,
                contractors: [],
                total_expenses: 0,
                project_site_boundaries: [],
                estimated_construction_start_date: null,
                construction_start_date: null,
                estimated_construction_completion_date: null,
                construction_completion_date: null,
                budget: 0,
                estimated_cost: 0,
                power_rating_gw: 1,
                notes: ''
            },
            isLoading: true,
            isContractorsLoading: true,
            contractorOptions: []
        };
    },
    computed: {
        projectId() {
            return this.$route.params.id;
        }
    },
    mounted() {
        if (this.projectId) {
            this.fetchProjectDetails();
        } else {this.isLoading = false}
        this.fetchContractors();
    },
    methods: {
        onUpdateBoundaries(coordinates) {
            this.project.project_site_boundaries = coordinates;
        },
        async fetchProjectDetails() {
            try {
                const response = await axios.get(`http://localhost:8000/api/projects/${this.projectId}/`);
                this.project = response.data;
                this.isLoading = false;
            } catch (error) {
                console.error('Error fetching project details:', error);
                this.isLoading = false;
            }
        },
        async fetchContractors() {
            try {
                const response = await axios.get('http://localhost:8000/api/contractors/');
                this.contractorOptions = response.data;
                this.isContractorsLoading = false;
            } catch (error) {
                console.error('Error fetching contractors:', error);
                this.isContractorsLoading = false;
            }
        },
        async onSubmit() {
            try {
                let response;
                if (this.projectId) {
                    // Update existing project
                    response = await axios.put(`http://localhost:8000/api/projects/${this.projectId}/`, this.project);
                } else {
                    // Create new project
                    response = await axios.post('http://localhost:8000/api/projects/', this.project);
                }
                console.log('Project saved successfully:', response.data);
                Notify.create({
                    type: 'positive',
                    message: 'Project saved successfully!'
                });
                this.$router.push(`/projects/${response.data.id}`);

            } catch (error) {
                console.error('Error saving project:', error);
                Notify.create({
                    type: 'negative',
                    message: 'Error saving project'
                });
            }
        },
        async onDelete() {
            try {
                await axios.delete(`http://localhost:8000/api/projects/${this.projectId}/`);
                Notify.create({
                    type: 'positive',
                    message: 'Project deleted successfully!'
                });
                this.$router.push('/projects'); // Redirect to projects list or any other page
            } catch (error) {
                console.error('Error deleting project:', error);
                Notify.create({
                    type: 'negative',
                    message: 'Error deleting project'
                });
            }
        }
    }
};
</script>

<style scoped></style>
