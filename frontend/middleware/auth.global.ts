import { useAuthStore } from '@/stores/auth'

export default defineNuxtRouteMiddleware(async (to, from) => {
    const authStore = useAuthStore()

    if (to.path.startsWith('/dashboard')) {
        const isValid = await authStore.verifySession()
        if (!isValid) {
            return navigateTo('/')
        }
    }
})
