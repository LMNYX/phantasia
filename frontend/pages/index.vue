<script lang="ts" setup>
import { ref } from 'vue'
import { useApiUrl } from '@/composables/useApiUrl'

const userAmount = ref(0)

const { internalApiBase } = useApiUrl()
const { data: userCount } = await useFetch<{ count: number }>(`${internalApiBase}/users/count`, { key: 'user-count' });
</script>
<template>
    <div class="main-page-content">
        <h1>Really Cute File Uploader</h1>
        <p>Only way {{ userCount?.count }} people know how to upload files now</p>
    </div>
</template>