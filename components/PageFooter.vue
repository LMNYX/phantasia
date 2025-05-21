<template>
  <div class="footer">
    <NuxtLink href="#" :class="{ active: isRouteActive('/') }">Home</NuxtLink>
    <NuxtLink href="#" :class="{ active: isRouteActive('/about') }">About</NuxtLink>
    <NuxtLink href="#" :class="{ active: isRouteActive('/faq') }">FAQ</NuxtLink>
    <NuxtLink href="#" class="right-aligned-button" @click.prevent="toggleDashboard" :class="{ active: isDashboardLoginPanelActive }">Dashboard</NuxtLink>
    <div class="dashboard-login-board" :class="{ active: isDashboardLoginPanelActive }">
      <div>
        <input placeholder="Access Key" type="password" v-show="!isAuthContentHidden">
        <button v-show="!isAuthContentHidden" @click="tryLogin">Auth</button>
        <p v-show="isAuthContentHidden">{{ authErrorMessage }}</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { useRoute } from 'vue-router'

const isDashboardLoginPanelActive = ref(false)

const toggleDashboard = () => {
  isDashboardLoginPanelActive.value = !isDashboardLoginPanelActive.value
}

const route = useRoute()

const isRouteActive = (path: string) => {
  return route.path === path && !isDashboardLoginPanelActive.value
}

const isAuthContentHidden = ref(false)
const authErrorMessage = ref('')

const tryLogin = async () =>
{
  isAuthContentHidden.value = true
  authErrorMessage.value = 'Example error message.'
}
</script>

<style>

</style>