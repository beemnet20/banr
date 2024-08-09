<template>
  <q-card class="q-pa-md q-ma-sm highlight-card col">
    <q-card-section>
      <div class="row items-center">
        <!-- Large Numeric Value -->
        <div class="">
          <span class="text-h3">{{ value }}</span>
        </div>
        <!-- Smaller Text Description -->
        <div class="">
          <span class="text-h6">{{ description }}</span>
        </div>
      </div>
    </q-card-section>
  </q-card>
</template>

<script>
export default {
  props: {
    value: {
      type: Number,
      required: true
    },
    description: {
      type: String,
      required: true
    }
  }
}
</script>

<style lang="sass" scoped>
.highlight-card
  min-width: 100px
  max-height: 200px
</style>