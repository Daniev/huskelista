<script lang="ts">
	import { goto } from '$app/navigation';
	import type { User } from '$lib/types/user';

	const setUser = (user: User) => {
		document.cookie = 'user=' + user;
		goto('/home');
	};
</script>

<section>
	<h1>Hvem er du?</h1>
	<div>
		<button class="dani" on:click={() => setUser('Daniel')}>Daniel</button>
		<button class="mia" on:click={() => setUser('Mia')}>Mia</button>
	</div>
</section>

<style lang="scss">
	section {
		height: 100svh;
		width: 100svw;
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}

	div {
		display: flex;
		flex-direction: row;
		align-items: center;
		justify-content: center;
	}

	button {
		--_bg: var(--bg-color-button, var(--mia-profile-color));
		margin: 1rem;
		height: 12rem;
		width: 23rem;
		font-size: var(--fo-xlarge);
		font-family: var(--header-font);
		line-height: var(--header-line-height);
		font-weight: 500;
		letter-spacing: var(--header-letter-spacing);
		background-color: var(--grey);
		&:hover {
			background-color: var(--_bg);
			color: var(--white-text-color);
			font-weight: 700;
		}
	}

	.dani {
		margin-right: 5rem;
		--bg-color-button: var(--daniel-profile-color);
	}
</style>
