<script lang="ts">
	import { user } from '$lib/stores/user';
</script>

<div class=" center">
	<h1 class="centerDown">Velkommen {$user}</h1>

	<section>
		<div class="todo">
			<h2>Gjøremål</h2>
			<ul>
				<li>Vask bad</li>
				<li>Kjøkken</li>
			</ul>
		</div>

		<div class="completed">
			<h2>Fullført</h2>
			<ul>
				<li>Re opp sengetøy</li>
				<li>Støvsuger og tørke støv</li>
			</ul>
		</div>
	</section>
</div>

<style lang="scss">
	section {
		height: 100vh;
		width: 100vw;
		display: flex;
		flex-direction: row;
		justify-content: space-around;
	}
</style>
