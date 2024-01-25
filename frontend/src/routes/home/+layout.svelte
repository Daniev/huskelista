<script lang="ts">
	import Button from '$lib/components/Button.svelte';
	import LeftSideMenu from '$lib/components/LeftSideMenu.svelte';
	import { user } from '$lib/stores';
	const logout = () => {
		$user = 'unknown';
		document.cookie = 'user=unknown';
	};
</script>

<header>
	<LeftSideMenu />
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
		justify-content: space-between;
		align-items: center;
		background-color: var(--matt-green);
		margin: 0;
		padding: 0;
	}

	a {
		margin: 0 var(--ma-big);
	}
	img {
		height: 3.5rem;
	}
</style>
