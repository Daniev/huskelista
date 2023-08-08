<script lang="ts">
	import { user } from '$lib/stores/user';
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
		background-color: $grey1;
		margin-right: 5rem;
		&:hover {
			background-color: $grey2;
		}
	}

	.mia {
		background-color: $pink;
		&:hover {
			background-color: $pink1;
		}
	}
</style>
