<script lang="ts">
	import ListEntry from '$lib/components/ListEntry.svelte';
	import TaskBox from '$lib/components/taskBox.svelte';
	import { user } from '$lib/stores/user';

	import { list } from '$lib/stores/lists';
	import { fly } from 'svelte/transition';
</script>

<div class=" center">
	<h1 class="centerDown">Velkommen {$user}</h1>

	<section>
		<TaskBox title="Gjøremål">
			<div slot="taskList">
				{#each $list as task}
					{#if task.completed === false}
						<div transition:fly={{ x: 500, duration: 200 }}>
							<ListEntry bind:task />
						</div>
					{/if}
				{/each}
			</div>
			<div slot="bottom">
				<button class="new">Ny</button>
			</div>
		</TaskBox>

		<TaskBox title="Fullført">
			<div slot="taskList">
				{#each $list as task}
					{#if task.completed}
						<div transition:fly={{ x: -500, duration: 200 }}>
							<ListEntry color="lightgrey" bind:task />
						</div>
					{/if}
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
