<script lang="ts">
	import ListEntry from '$lib/components/ListEntry.svelte';
	import TaskBox from '$lib/components/taskBox.svelte';
	import NewTaskDropdown from '$lib/components/NewTaskDropdown.svelte';

	import { fly } from 'svelte/transition';
	import { list, user } from '$lib/stores';

	let showComplete = true;

	const toggleShow = () => {
		showComplete = !showComplete;
	};
</script>

<div class=" center">
	<h1 class="centerDown">Velkommen {$user}</h1>

	<section>
		<TaskBox title="Gjøremål">
			<div slot="taskList">
				{#each $list as task}
					{#if task.completed === false}
						<div transition:fly={{ x: 500, duration: 200 }}>
							{#if $user === 'Daniel'}
								<ListEntry classes="daniel" bind:task />
							{:else if $user === 'Mia'}
								<ListEntry classes="mia" bind:task />
							{/if}
						</div>
					{/if}
				{/each}
			</div>
			<div slot="bottom">
				<NewTaskDropdown />
			</div>
		</TaskBox>

		<div>
			<div class="header">
				<h2>Fullførte</h2>
				{#if !showComplete}
					<button on:click={toggleShow}>Vis</button>
				{:else}
					<button on:click={toggleShow}>Skjul</button>
				{/if}
			</div>
			{#if showComplete}
				{#each $list as task}
					{#if task.completed}
						<div transition:fly={{ x: -500, duration: 200 }}>
							<ListEntry bind:task />
						</div>
					{/if}
				{/each}
			{/if}
		</div>
	</section>
</div>

<style lang="scss">
	section {
		display: flex;
		flex-direction: column;
		justify-content: center;
		align-items: center;

		.header {
			display: flex;
			justify-content: space-between;
			align-items: center;
			width: 22rem;

			button {
				padding: 0.5rem 1rem;
			}
		}
	}
</style>
