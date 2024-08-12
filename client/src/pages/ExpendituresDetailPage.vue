<template>
    <q-page class="q-pa-md">
        <div class="text-h6 q-ma-md">
            {{ expenditureId ? `expenditure: ${expenditure.expense_name}` : 'Add a new expense' }}
        </div>

        <q-form @submit="onSubmit" class="q-gutter-md q-mt-md">
            <div class="row">
                <div class="col-12 col-md-6">
                    <q-select :rules="[val => !!val || 'Project is required']" class="q-ma-sm" filled v-model="expenditure.project" :options="projectOptions" label="Project" option-label="project_name" option-value="id" emit-value />
                    <q-input :rules="[val => !!val || 'Expense name is required']" class="q-ma-sm" filled v-model="expenditure.expense_name" label="Expense name"
                        :disable="isLoading" />
                    <q-input :rules="[val => !!val || 'Amount is required']" type="number" class="q-ma-sm" filled v-model="expenditure.amount" label="Amount"
                        :disable="isLoading" />
                    <q-select class="q-ma-sm" :options="expenditureCategories" filled v-model="expenditure.category"
                        label="Category" :disable="isLoading" />
                </div>
                <div class="col-12 col-md-6">
                    <q-select class="col q-ma-sm"  filled v-model="expenditure.contractors" label="Contractors"
                        :options="contractorOptions" option-value="id" option-label="company_name" emit-value
                        map-options :disable="isLoading || isContractorsLoading" />
                    <q-input class="col q-ma-sm" type="date" v-model="expenditure.date_incurred" filled
                        label="Date incurred" :disable="isLoading" />
                    <q-input class="col q-ma-sm" type="number" v-model="expenditure.description" filled label="Description"
                        :disable="isLoading" />

                </div>
            </div>

            <div class="row">
                <q-btn v-if="expenditureId" type="button" class="col q-ma-sm"  label="Delete expense"  color="negative" @click="onDelete" :disable="isLoading" />

                <q-btn class="col q-ma-sm" type="submit" label="Save expenditure" color="primary"
                    :disable="isLoading" />
            </div>
        </q-form>
    </q-page>
</template>

<script>
import axios from 'axios';
import { Notify } from 'quasar';

export default {
    setup() {
        return {
            expenditureCategories: ["materials", "labor", "equipment", "other"]
        }
    },
    data() {
        return {
            expenditure: {
                expense_name: '',
                amount: 0,
                project: null,
                date_incurred: null,
                description: '',
                contractor: null,
                category: null
            },
            isLoading: true,
            isContractorsLoading: true,
            contractorOptions: [],
            isProjectLoading: true,
            projectOptions: []
        };
    },
    computed: {
        expenditureId() {
            return this.$route.params.id;
        }
    },
    mounted() {
        if (this.expenditureId) {
            this.fetchExpenditureDetails();
        } else { this.isLoading = false }
        this.fetchContractors();
        this.fetchProjects();
    },
    methods: {
        async fetchExpenditureDetails() {
            try {
                const response = await axios.get(`http://localhost:8000/api/expenditures/${this.expenditureId}/`);
                this.expenditure = response.data;
                this.isLoading = false;
            } catch (error) {
                console.error('Error fetching expenditure details:', error);
                this.isLoading = false;
                if (error.response.status === 404) {
                    this.$router.replace({ path: '/404' });
                }
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
        async fetchProjects() {
            try {
                const response = await axios.get('http://localhost:8000/api/projects/');
                this.projectOptions = response.data;
                this.isProjectLoading = false;
            } catch (error) {
                console.error('Error fetching projects:', error);
                this.isProjectLoading = false;
            }
        },
        async onSubmit() {
            try {
                let response;
                if (this.expenditureId) {
                    // Update existing expenditure
                    response = await axios.put(`http://localhost:8000/api/expenditures/${this.expenditureId}/`, this.expenditure);
                } else {
                    // Create new expenditure
                    response = await axios.post('http://localhost:8000/api/expenditures/', this.expenditure);
                }
                console.log('expenditure saved successfully:', response.data);
                Notify.create({
                    type: 'positive',
                    message: 'expenditure saved successfully!'
                });
                this.$router.push(`/expenditures/${response.data.id}`);

            } catch (error) {
                console.error('Error saving expenditure:', error);
                Notify.create({
                    type: 'negative',
                    message: 'Error saving expenditure'
                });
            }
        },
        async onDelete() {
            try {
                await axios.delete(`http://localhost:8000/api/expenditures/${this.expenditureId}/`);
                Notify.create({
                    type: 'positive',
                    message: 'expenditure deleted successfully!'
                });
                this.$router.push('/expenditures');
            } catch (error) {
                console.error('Error deleting expenditure:', error);
                Notify.create({
                    type: 'negative',
                    message: 'Error deleting expenditure'
                });
            }
        }
    }
};
</script>

<style scoped></style>
