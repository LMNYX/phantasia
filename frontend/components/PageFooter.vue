<template>
  <div class="footer">
    <NuxtLink href="/" draggable="false" :class="{ active: isRouteActive('/') }">Home</NuxtLink>
    <NuxtLink href="/about" draggable="false" :class="{ active: isRouteActive('/about') }">About</NuxtLink>
    <NuxtLink href="/faq" draggable="false" :class="{ active: isRouteActive('/faq') }">FAQ</NuxtLink>
    <NuxtLink href="#" draggable="false" class="right-aligned-button" @click.prevent="toggleDashboard" :class="{ active: isDashboardLoginPanelActive || isRouteActive('/dashboard') }">Dashboard</NuxtLink>
    <div class="dashboard-login-board" :class="{ active: isDashboardLoginPanelActive }">
      <div>
        <input v-model="accessKeyInput" placeholder="Access Key" type="password" :disabled="isAuthContentDisabled" v-show="!isAuthContentHidden">
        <button v-show="!isAuthContentHidden" :disabled="isAuthContentDisabled" @click="tryLogin">Auth</button>
        <p v-show="isAuthContentHidden">{{ authErrorMessage }}</p>
      </div>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref } from 'vue'
import { useApiUrl } from '@/composables/useApiUrl'
import { useRoute, useRouter } from 'vue-router'
import { useAuthStore } from '@/stores/auth'

const authStore = useAuthStore()
const router = useRouter()
const accessKeyInput = ref('')
const isDashboardLoginPanelActive = ref(false)
const isAuthContentDisabled = ref(false)

const toggleDashboard = () => {
  if (authStore.isLoggedIn) {
    router.push('/dashboard')
    isDashboardLoginPanelActive.value = false
    return
  }
  isDashboardLoginPanelActive.value = !isDashboardLoginPanelActive.value
}

const route = useRoute()

const isRouteActive = (path: string) => {
  return route.path === path && !isDashboardLoginPanelActive.value
}

const isAuthContentHidden = ref(false)
const authErrorMessage = ref('')

const tryLogin = async () => {
  if (!accessKeyInput.value) {
    setLoginError('Please enter an access key')
    return
  }

  const { apiBase } = useApiUrl()
  try {
    const data = await $fetch<{ authenticated: boolean; user: any }>(`${apiBase}/users/authenticate`, {
      params: { access_key: accessKeyInput.value }
    })

    if (data.authenticated) {
      authStore.setSession(data.user, accessKeyInput.value)
      isDashboardLoginPanelActive.value = false
      router.push('/dashboard')
    }
  } catch (error: any) {
    if(!error.data.authenticated)
    {
      setLoginError('Invalid access key')
    }
    else
    {
      setLoginError('An error occurred during authentication')
    }
  } finally {
    isAuthContentDisabled.value = false
    accessKeyInput.value = ''
  }
}

function setLoginError(errorMessage: string)
{
  isAuthContentHidden.value = true
  authErrorMessage.value = errorMessage

  setTimeout(() => {
    authErrorMessage.value = ""
    isAuthContentHidden.value = false
  }, 2222);
}
</script>

<style>

</style>