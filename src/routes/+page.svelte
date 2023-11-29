<script lang="ts">
	import { user } from '$lib/stores';
</script>

<section>
	<h1>Hvem er du?</h1>

	<div>
		<a href="/home">
			<button class="dani" on:click={() => ($user = 'Daniel')}>Daniel</button>
		</a>

		<a href="/home">
			<button class="mia" on:click={() => ($user = 'Mia')}>Mia</button>
		</a>
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
		font-size: $font-xl;
		font-weight: bold;
	}

	.dani {
		background-color: var(--light-green);
		margin-right: 5rem;
		&:hover {
			background-color: var(--light-green-darker);
		}
	}

	.mia {
		background-color: var(--yellow);
		&:hover {
			background-color: var(--yellow-darker);
		}
	}
</style>
