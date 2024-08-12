<template>
    <q-card-section class="q-pa-none">
        <div id="map" class="map-container"></div>
    </q-card-section>
</template>

<script>
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import "leaflet-draw/dist/leaflet.draw.css";
import "leaflet-draw/dist/leaflet.draw-src.js";

import axios from 'axios';

export default {
    props: {
        zipcode: {
            type: String,
            required: true,
        },
        projectSiteBoundaries: {
            type: Array,
            default: () => [],
        },
    },
    data() {
        return {
            map: null,
            drawnItems: null,
        };
    },
    mounted() {
        this.initializeMap();
    },
    methods: {
        async initializeMap() {
            // Initialize the map centered on the USA
            this.map = L.map('map', { attributionControl: false }).setView([37.8, -96], 4);

            // Add a tile layer to the map
            L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
                maxZoom: 19,
            }).addTo(this.map);

            // Fetch the latitude and longitude using the API
            const response = await axios.get('http://localhost:8000/api/get-lat-lon', { params: { zipcode: this.zipcode } });
            const data = response.data;
            if (data) {
                const lat = data.latitude;
                const lon = data.longitude;

                // Center the map on the fetched location
                this.map.setView([lat, lon], 13);

                // Add existing polygons if any
                this.drawnItems = new L.FeatureGroup().addTo(this.map);
                if (this.projectSiteBoundaries) {
                    L.polygon(this.projectSiteBoundaries).addTo(this.drawnItems);
                }

                // Add draw control
                const drawControl = new L.Control.Draw({
                    edit: {
                        featureGroup: this.drawnItems,
                    },
                    draw: {
                        polygon: true,
                        marker: false,
                        polyline: false,
                        rectangle: false,
                        circle: false,
                        circlemarker: false,
                    },
                });
                this.map.addControl(drawControl);

                // Save drawn polygons
                this.map.on('draw:created', (e) => {
                    const layer = e.layer;
                    this.drawnItems.addLayer(layer);
                    this.$emit('update-boundaries', layer.getLatLngs()[0].map(obj => [obj.lat, obj.lng]));
                });

                this.map.on('draw:edited', (e) => {
                    const layers = e.layers;
                    layers.eachLayer((layer) => {
                        this.$emit('update-boundaries', layer.getLatLngs()[0].map(obj => [obj.lat, obj.lng]));
                    });
                });
            }
        },
    },
};
</script>

<style scoped>
.map-container {
    min-height: 375px;
    height: 100%;
    width: 100%;
}
</style>