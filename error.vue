<script setup lang="ts">
import type { NuxtError } from '#app'

const props = defineProps({
  error: Object as () => NuxtError
})
</script>

<template>
    <main class="page">
        <div class="main">
            <div class="main-page-content">
                <h1>{{error.statusCode}}</h1>
                <p>There has been an error trying to get this page!</p>
                <p>{{error}}</p>
            </div>
        </div>
    </main>
</template>
