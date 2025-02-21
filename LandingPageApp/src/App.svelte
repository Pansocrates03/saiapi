<script lang="ts">
  import Navigation from './lib/sections/Navigation.svelte';
  import Hero from './lib/sections/Hero.svelte';
  import Footer from './lib/sections/Footer.svelte';
  import AttributeSection from './lib/sections/AttributeSection.svelte';
</script>

<header style="height: 100vh;">
  <Navigation />
  <Hero />
  <div class="heroFooter">
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fc/Flag_of_Mexico.svg/1200px-Flag_of_Mexico.svg.png" alt="Mexico flag" style="width: 5vw;" />
    Mexican Sign Language
  </div>
</header>

<AttributeSection />
<div class="callToAction"></div>
<Footer />

<style>

  header {
    display: flex;
    flex-direction: column;
    justify-content: space-between;
    align-items: center;
  }

  .heroFooter {
    width: 100%;
    background-color: white;
    border-top: 1px solid #333;
    border-bottom: 1px solid #333;
  }  

</style>
