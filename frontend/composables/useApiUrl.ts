export const useApiUrl = () => {
    const url = useRequestURL()
    const host = url.host
    const protocol = url.protocol

    const apiBase = `${protocol}//api.${host}`
    const imageBase = `${protocol}//i.${host}`

    // Internal API URL for SSR to communicate between containers
    const internalApiBase = import.meta.server ? 'http://phantasia-api:4444' : apiBase

    return {
        apiBase,
        imageBase,
        internalApiBase
    }
}
