<template>
    <div class="central-content">
      <h1>FAQ</h1>
      <p><i>aka what i cant be asked to answer</i></p>
      <br>
      <h2>I forgot my key</h2>
      <p>I am working on implementing resetting of keys without administrator contact, but as of now you have to contact one of the administrators to get a reset link.</p>
      <h2>I found my copyrighted material on your website</h2>
      <p>Please contact <NuxtLink to="mailto:me@reze.moe">me@reze.moe</NuxtLink> (me@reze.moe) with a <b>[DMCA]</b> in the subject. Attach any proof of ownership of the material and infringing links.</p>
      <h2>Can I get access?</h2>
      <p>If you have to ask, no.</p>
      <h2>Can I support you?</h2>
      <p>Yes. Visit <NuxtLink to="https://mishashto.com/donate">this page</NuxtLink> to learn more.</p>
      <h2>Why is it down or slow sometimes?</h2>
      <p>Downtime is as rare as we can possibly get, excluding the daily morning restart (Sweden morning). Slowness may be due to Telia being morons or you're far away from Sweden. If you want to contribute to stability, please inquire with <NuxtLink to="https://pavel.gg">NekoPavel</NuxtLink> on how you can donate.</p>
      <h2>Can I read Privacy Policy or Terms of Service?</h2>
      <p>I use the same terms of service for all my projects. You can read them <NuxtLink to="https://mishashto.com/terms">here</NuxtLink>.</p>
      <h2>Is this open-source?</h2>
      <p>Imagination Server is open-source Since September 19th, 2023. Please look at <NuxtLink to="https://github.com/orgs/GoofyGoofsterClub/repositories">our GitHub organization's</NuxtLinK> repositories. Phantasia Media Uploader is yet to be public.</p>
      <h2>Is there public API?</h2>
      <p>Not yet.</p>
      <h2>Is there file size limit?</h2>
      <p>No, but do not upload all seasons of RuPaul's Drag Race. Humanity invented common sense for a reason.</p>
      <h2>How do I set this up?</h2>
      <p>For ShareX please open your dashboard and download the settings file and import it in ShareX. For Chatterino:</p>
      <p>
        <ul><li>Request URL: https://api.uwu.so/uploads/create</li>
        <li>Form field: image</li>
        <li>Extra headers: Authorization: YOURKEY</li>
        <li>Image link: {data.link}</li></ul>
      </p>
    </div>
</template>

<script lang="ts" setup>

</script>

<style>

</style>