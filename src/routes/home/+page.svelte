<script lang="ts">
	import ListEntry from '$lib/components/ListEntry.svelte';
	import TaskBox from '$lib/components/taskBox.svelte';
	import { user } from '$lib/stores/user';

	const list1: string[] = ['vask bad', 'kjøkken'];
	const completeList: string[] = ['Re opp senger', 'Støvsuger og tørke støv'];
</script>

<div class=" center">
	<h1 class="centerDown">Velkommen {$user}</h1>

	<section>
		<TaskBox title="Gjøremål">
			<div slot="taskList">
				{#each list1 as item}
					<ListEntry>{item}</ListEntry>
				{/each}
			</div>
			<div slot="bottom">
				<button class="new">Ny</button>
			</div>
		</TaskBox>

		<TaskBox title="Fullført">
			<div slot="taskList">
				{#each completeList as item}
					<ListEntry color="lightgrey">{item}</ListEntry>
				{/each}
			</div>
		</TaskBox>
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

	.new {
		border-radius: $border-lg;
		height: 2rem;
		width: 2rem;
		background-color: $button-color;
		color: $white;
		&:hover {
			background-color: $button-hover-color;
		}
	}
</style>
