<template>
  <q-layout view="lHh Lpr lFf">
    <q-header elevated>
      <q-toolbar>
        <q-btn
          flat
          dense
          round
          icon="menu"
          aria-label="Menu"
          @click="toggleLeftDrawer"
        />

        <q-toolbar-title>
          banr
        </q-toolbar-title>

      </q-toolbar>
    </q-header>

    <q-drawer
      v-model="leftDrawerOpen"
      show-if-above
      bordered
    >
      <q-list>
        <EssentialLink
          v-for="link in linksList"
          :key="link.title"
          v-bind="link"
        />
      </q-list>
    </q-drawer>

    <q-page-container>
      <router-view />
    </q-page-container>
  </q-layout>
</template>

<script setup>
import { ref } from 'vue'
import EssentialLink from 'components/EssentialLink.vue'

defineOptions({
  name: 'MainLayout'
})

const linksList = [
  {
    title: 'Home',
    icon: 'home',
    link: '/'
  },
  {
    title: 'Projects',
    icon: 'build',
    link: '/projects'
  },
  {
    title: 'Expenditures',
    icon: 'paid',
    link: '/expenditures'
  },
  {
    title: 'Contractors',
    icon: 'engineering',
    link: '/contractors'
  }
]

const leftDrawerOpen = ref(false)

function toggleLeftDrawer () {
  leftDrawerOpen.value = !leftDrawerOpen.value
}
</script>
