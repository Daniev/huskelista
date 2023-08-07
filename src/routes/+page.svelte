<script lang="ts">
	import { user } from '$lib/stores/user';
</script>

<section>
	<h1>Hvem er du?</h1>

	<div>
		<a href="/home">
			<button on:click={() => ($user = 'Daniel')}>Daniel</button>
		</a>

		<a href="/home">
			<button on:click={() => ($user = 'Mia')}>Mia</button>
		</a>
	</div>
</section>

<style lang="scss">
	h1 {
		font-size: 48px;
	}

	a {
		text-decoration: none;
	}
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
		height: 15rem;
		width: 30rem;

		font-size: 32px;
	}
</style>
