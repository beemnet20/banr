<template>
    <q-page class="q-pa-md">
        <div class="text-h6 q-ma-md">
            {{ contractorId ? `contractor: ${contractor.company_name}` : 'Add a new contractor' }}
        </div>

        <q-form @submit="onSubmit" class="q-gutter-md q-mt-md">
            <div class="row">
                <div class="col-12 col-md-6">
                    <q-input :rules="[val => !!val || 'Company name is required']" class="q-ma-sm" filled v-model="contractor.company_name" label="Company name"
                        :disable="isLoading" type="text" />
                    <q-input  type="text" class="q-ma-sm" filled v-model="contractor.field_of_work" label="Field of work"
                        :disable="isLoading" />
                    <q-input  type="text" class="q-ma-sm" filled v-model="contractor.contact_person" label="Contact person"
                        :disable="isLoading" />
                    <q-input  type="tel" class="q-ma-sm" filled v-model="contractor.phone_number" label="Phone number"
                        :disable="isLoading" />
                    <q-input  type="email" class="q-ma-sm" filled v-model="contractor.email" label="email"
                        :disable="isLoading" />
                    

                </div>
            </div>

            <div class="row">
                <q-btn v-if="contractorId" type="button" class="col q-ma-sm"  label="Remove contractor"  color="negative" @click="onDelete" :disable="isLoading" />

                <q-btn class="col q-ma-sm" type="submit" label="Save contractor" color="primary"
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
            contractorCategories: ["materials", "labor", "equipment", "other"]
        }
    },
    data() {
        return {
            contractor: {
                company_name: '',
                field_of_work: '',
                contact_person: '',
                phone_number: '',
                email: '',
            },
            isLoading: true,
        };
    },
    computed: {
        contractorId() {
            return this.$route.params.id;
        }
    },
    mounted() {
        if (this.contractorId) {
            this.fetchContractorDetails();
        } else { this.isLoading = false }
    },
    methods: {
        async fetchContractorDetails() {
            try {
                const response = await axios.get(`http://localhost:8000/api/contractors/${this.contractorId}/`);
                this.contractor = response.data;
                this.isLoading = false;
            } catch (error) {
                console.error('Error fetching contractor details:', error);
                this.isLoading = false;
                if (error.response.status === 404) {
                    this.$router.replace({ path: '/404' });
                }
            }
        },
        async onSubmit() {
            try {
                let response;
                if (this.contractorId) {
                    // Update existing contractor
                    response = await axios.put(`http://localhost:8000/api/contractors/${this.contractorId}/`, this.contractor);
                } else {
                    // Create new contractor
                    response = await axios.post('http://localhost:8000/api/contractors/', this.contractor);
                }
                console.log('contractor saved successfully:', response.data);
                Notify.create({
                    type: 'positive',
                    message: 'contractor saved successfully!'
                });
                this.$router.push(`/contractors/${response.data.id}`);

            } catch (error) {
                console.error('Error saving contractor:', error);
                Notify.create({
                    type: 'negative',
                    message: 'Error saving contractor'
                });
            }
        },
        async onDelete() {
            try {
                await axios.delete(`http://localhost:8000/api/contractors/${this.contractorId}/`);
                Notify.create({
                    type: 'positive',
                    message: 'contractor deleted successfully!'
                });
                this.$router.push('/contractors');
            } catch (error) {
                console.error('Error deleting contractor:', error);
                Notify.create({
                    type: 'negative',
                    message: 'Error deleting contractor'
                });
            }
        }
    }
};
</script>

<style scoped></style>
