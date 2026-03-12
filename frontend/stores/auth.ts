import { defineStore } from 'pinia'
import { ref } from 'vue'

export interface AuthContext {
    id: number
    username: string
    permissions: string[]
    is_banned: boolean
}

export const useAuthStore = defineStore('auth', () => {
    const session = useCookie<AuthContext | null>('session')
    const accessKey = useCookie<string | null>('accessKey')
    const isLoggedIn = ref(!!session.value && !!accessKey.value)

    function setSession(user: AuthContext | null, key: string | null) {
        session.value = user
        accessKey.value = key
        isLoggedIn.value = !!user && !!key
    }

    function logout() {
        session.value = null
        accessKey.value = null
        isLoggedIn.value = false
    }

    async function verifySession() {
        if (!accessKey.value) {
            logout()
            return false
        }

        const { internalApiBase } = useApiUrl()
        try {
            const data = await $fetch<{ authenticated: boolean, user: AuthContext | null }>(`${internalApiBase}/users/authenticate`, {
                params: { access_key: accessKey.value }
            })

            if (data.authenticated && data.user && !data.user.is_banned) {
                setSession(data.user, accessKey.value)
                return true
            } else {
                logout()
                return false
            }
        } catch (error) {
            console.error('Session verification failed:', error)
            logout()
            return false
        }
    }

    return { session, accessKey, isLoggedIn, setSession, logout, verifySession }
})