<script lang="ts" setup>
import { ref } from 'vue'

const userAmount = ref(0)
</script>
<template>
    <div class="main-page-content">
        <h1>Really Cute File Uploader</h1>
        <p>Only way {{ userAmount }} people know how to upload files now</p>
    </div>
</template>