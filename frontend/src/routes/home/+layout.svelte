<script lang="ts">
	import Button from '$lib/components/Button.svelte';
	import { user } from '$lib/stores';
	const logout = () => {
		$user = 'unknown';
		document.cookie = 'user=unknown';
	};
</script>

<header>
	<img src="Logo.png" alt="logo" />
	<a href="/">
		<Button on:click={logout}>Logg ut</Button>
	</a>
</header>

<slot />

<style lang="scss">
	header {
		width: 100svw;
		height: 3.8rem;
		display: flex;
		justify-content: right;
		align-items: center;
		background-color: var(--matt-green);
	}

	a {
		margin: 0 var(--ma-big);
	}
	img {
		height: 3.5rem;
		margin-right: 41.5svw;
	}
</style>
