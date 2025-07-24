<template>
    <div class="central-content">
      <h1>About</h1>
      <p><i>aka history of the service</i></p>
      <br>
      <div class="slim-content">
        <p>This is a fourth iteration of a file uploader, that was previously referred to as <NuxtLink to="https://github.com/GoofyGoofsterClub/imagination-server">ImaginationServer</NuxtLink>. It offered file uploads for ShareX users and Chatterino users, as well as online upload at a later update. While we still offer that, we now offer more variable file manipulations and faster uploads and load times for files.</p>
        <p>It all started as a joke, when I, <NuxtLink to="https://mishashto.com">mishashto</NuxtLink>, bought a domain name that had female private parts in its name and .pics TLD and started uploading my images on it to share in Twitch chat, quickly after a lot of people wanted to have access to it and I was forced ot make a dumbed down NodeJS version with simple HTML and no CSS dashboard to allow people to control their uploads.</p>
        <p>After a year or so, Saudi Arabian government banned access to the service inside the country, presumably because of the domain name. To resolve the issue quickly, I bought another domain, <b>no</b>[femalepart].pics, and hosted a mirror with all references to obscenity being <i>halal</i>ified, as well as submitted an appeal to Saudi government. In about a month or two the main domain was unbanned and the mirror was abandoned.</p>
        <p>I added a lot of other domains as mirrors in the meantime, but the one that remained after the extremely expensive funny domain expired was <NuxtLink to="https://uwu.so">uwu.so</NuxtLink>. And with that all people moved to it and it stopped being a mirror.</p>
        <p>Service was hosted on AWS but the pricing and servers provided by AWS were honestly not the best, so the servers were transferred to the <NuxtLink to="https://pavel.gg">NekoPavel's</NuxtLink> home server, for which I'm still really thankful! The fact that his home server is alive keeps this service running for everyone else for free <i>(except me, and him)</i>.</p>
      </div>
      <br>
      <h2>Early contributors</h2>
      <p>Thanks to doritorainn, <NuxtLink to="https://m.twitch.tv/nephraa/home">Nephraa</NuxtLink>, <NuxtLink to="https://github.com/clevernt/">clever(nt)</NuxtLink>, <NuxtLink to="https://x.com/kanuiosu">kanui</NuxtLink>, UYCactus, <NuxtLink to="https://pavel.gg">NekoPavel</NuxtLink>, <NuxtLink to="https://www.twitch.tv/kexiv_">Kexiv</NuxtLink> and others for initially using the service and testing it!</p>
      <br>
      <p><span class="v-a">powered by</span><Icon class="v-a icon" name="mdi:soundcloud" /><span class="v-a">bangers</span></p>
    </div>
</template>

<script lang="ts" setup>

</script>

<style lang="scss" scoped>
.v-a
{
  cursor: default;
  user-select: none;
  vertical-align: middle;

  &.icon
  {
    margin: 0 6px;
    color: #ff5500;
  }
}
</style>