<script lang="ts">
    import Button from '../components/Button.svelte';
</script>

<div class="navContainer">
    <nav>
        <div class="logo">SaiLearning</div>
        <Button text="EMPIEZA AHORA" />
    </nav>
</div>

<style>
    .navContainer {
        border-bottom: #e2e2e2 solid 2px;
        width: 100vw;
    }
    
    
 nav {
    display: flex;
    justify-content: space-between;
    align-items: center;
    margin: 0 auto;
    max-width: 988px;
    height: 70px;
  }

  .logo {
    color: var(--color-primary);
    font-size: 2rem;
    font-weight: bold;
  }
</style>