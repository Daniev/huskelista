<script lang="ts">
	import ListEntry from '$lib/components/ListEntry.svelte';
	import TaskBox from '$lib/components/taskBox.svelte';
	import { user } from '$lib/stores/user';

	import { list } from '$lib/stores/lists';
	import { fly } from 'svelte/transition';
	import Dropdown from '$lib/components/Dropdown.svelte';
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
				<Dropdown>
					<button class="new" slot="button">Ny</button>
					<div class="dropdown-content" slot="content">
						<h2>Lag nytt gjøremål</h2>
						<input type="text" placeholder="Gjøremål" />
					</div>
				</Dropdown>
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
		background-color: var(--button-color);
		color: $white;
		&:hover {
			background-color: $button-hover-color;
		}
	}
</style>
