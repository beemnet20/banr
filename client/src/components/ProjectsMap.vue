<template>
  <q-card class="q-ma-md">
    <q-card-section>
      <div class="text-h6">Project locations</div>
    </q-card-section>

    <q-card-section class="q-pa-none">
      <div id="map" class="map-container"></div>
    </q-card-section>
  </q-card>
</template>

<script>
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import axios from 'axios';


export default {
  props: {
    projects: {
      type: Array,
      required: true,
      default: () => []
    }
  },
  mounted() {
    // Initialize the map
    const map = L.map('map').setView([39.8283, -98.5795], 4);

    // Add a tile layer to the map
    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
      maxZoom: 19,
    }).addTo(map);

    // Place pins on the map for each project
    this.projects.forEach(project => {
      this.addPinForzipcode(project.zipcode, project.city, map);
    });
  },
  methods: {
    async addPinForzipcode(zipcode, city, map) {
      // Use Nominatim geocoding API to get latitude and longitude from zipcode
      const response = await axios.get("http://localhost:8000/api/get-lat-lon", { params: { zipcode: zipcode } })
      const data = response.data
      if (data) {
        const lat = data.latitude;
        const lon = data.longitude;

        // Add a marker to the map at the geocoded location
        L.marker([lat, lon]).addTo(map)
          .bindPopup(`${city}`)
      }
    }
  }
}
</script>

<style scoped>
.map-container {
  height: 400px;
  /* Set a fixed height for the map */
  width: 100%;
  /* Make the map fill the card width */
}
</style>