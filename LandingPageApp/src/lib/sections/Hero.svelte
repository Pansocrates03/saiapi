<script>
  import svelteLogo from './../../assets/svelte.svg'
    import Button from '../components/Button.svelte'
    import heroImage from "./../../assets/Imagen1.png"
</script>

<div class="heroSection">
    <div class="left">
      <h1>Lengua de señas desde<br> la comodidad de su casa</h1>
      <Button text="EMPIEZA AHORA" style="primary" />
      <Button text="YA TENGO CUENTA" style="secondary" />
    </div>
    <div class="right">
      <img src={heroImage} alt="Svelte logo" style="width: 20vw;" />
    </div>
    
  </div>

<style>
    h1 {
        font-size: 2.5rem;
        font-weight: 700;
        margin-bottom: 1rem;
    }
    .heroSection {
        display: flex;
        flex-direction: row;
        flex-grow: 1;
        gap: 4rem;
    }
    .heroSection div {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
</style>