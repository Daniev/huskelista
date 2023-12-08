<script lang="ts">
	import { user } from '$lib/stores';
	const logout = () => {
		$user = 'unknown';
		document.cookie = 'user=unknown';
	};
</script>

<header>
	<a href="/">
		<button class="round" on:click={logout}>Logg ut</button>
	</a>
</header>

<slot />

<style lang="scss">
	header {
		width: 100vw;
		height: 8vh;
		display: flex;
		justify-content: right;
		align-items: center;
		background-color: var(--matt-green);
	}

	.round {
		margin-right: 2rem;
		height: 2rem;
		width: 6rem;
		border-radius: 84px;
		font-size: 16px;
		background-color: var(--subtle-button-color);

		&:hover {
			background-color: var(--subtle-button-hover-color);
		}
	}
</style>
