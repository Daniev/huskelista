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
		height: 100vh;
		width: 100vw;
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
		margin: 1rem;
		height: 12rem;
		width: 23rem;
		font-size: var(--fo-xlarge);
		font-family: var(--header-font);
		line-height: var(--header-line-height);
		letter-spacing: var(--header-letter-spacing);
	}

	.dani {
		background-color: var(--daniel-profile-color);
		margin-right: 5rem;
		&:hover {
			background-color: var(--daniel-profile-color-darker);
		}
	}

	.mia {
		background-color: var(--mia-profile-color);
		&:hover {
			background-color: var(--mia-profile-color-darker);
		}
	}
</style>
