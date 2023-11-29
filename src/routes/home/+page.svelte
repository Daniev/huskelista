<script lang="ts">
	import ListEntry from '$lib/components/ListEntry.svelte';
	import TaskBox from '$lib/components/taskBox.svelte';
	import NewTaskDropdown from '$lib/components/NewTaskDropdown.svelte';

	import { fly } from 'svelte/transition';
	import { list, user } from '$lib/stores';
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
				<NewTaskDropdown />
			</div>
		</TaskBox>

		<div>
			{#each $list as task}
				{#if task.completed}
					<div transition:fly={{ x: -500, duration: 200 }}>
						<ListEntry color="lightgrey" bind:task />
					</div>
				{/if}
			{/each}
		</div>
	</section>
</div>

<style lang="scss">
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;
	}
</style>
