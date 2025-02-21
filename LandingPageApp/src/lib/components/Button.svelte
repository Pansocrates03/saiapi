<script lang="ts">
    export let text = 'Click me';
    export let onClick = () => {};
    export let disabled = false;
    export let type: 'button' | 'submit' | 'reset' = 'button';
    export let style: "primary" | "secondary" | "outlined" = "primary";
</script>

<button
    type={type}
    on:click={onClick}
    disabled={disabled}
    class={style}>
    {text}
</button>

<style>
    button {
        font-size: 1rem;
        font-weight: 600;
        text-transform: uppercase;
        cursor: pointer;
        outline: none;
        padding-top: 1rem;
        padding-bottom: 1rem;
        width: 13rem;
        border-radius: 5px;
        stroke-width: 10px;
    }

    .primary {
        background-color: var(--color-primary);
        color: white;
        border: none;
    }
    .secondary {
        background-color: white;
        color: var(--color-primary);
        border: 1px solid var(--color-primary);
    }
    .outlined {
        background-color: transparent;
        color: var(--color-primary);
        border: 1px solid var(--color-primary);
    }
</style>