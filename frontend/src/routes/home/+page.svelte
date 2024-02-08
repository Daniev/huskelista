<script lang="ts">
	import ListEntry from '$lib/components/ListEntry.svelte';
	import TaskBox from '$lib/components/taskBox.svelte';
	import NewTaskDropdown from '$lib/components/NewTaskDropdown.svelte';
	import Button from '$lib/components/Button.svelte';

	import { fly } from 'svelte/transition';
	import { list, user, quickList } from '$lib/stores';
	import Icon from '$lib/components/Icon.svelte';
	import Trash from '$lib/components/Trash.svelte';

	export let data;

	let showComplete = true;
	let iconName = 'zondicons:cheveron-up';
	$: $user = data.user;
	$: $list = data.response;
	$: $quickList = data.quick_response;
	$: iconName = showComplete ? 'zondicons:cheveron-up' : 'zondicons:cheveron-down';

	const toggleShow = () => {
		showComplete = !showComplete;
	};
</script>

<div class="center">
	<h1 class="centerDown">Velkommen {$user}</h1>

	<section>
		<TaskBox title="Gjøremål">
			<div slot="taskList">
				{#each $list as task}
					{#if task.complete === false}
						<div transition:fly={{ x: 500, duration: 200 }}>
							{#if $user === 'Daniel'}
								<ListEntry classes="daniel" bind:task />
							{:else if $user === 'Mia'}
								<ListEntry classes="mia" bind:task />
							{/if}
						</div>
					{/if}
				{/each}
				{#if $list.filter((t) => t.complete === false).length === 0}
					<div class="none">Ingen gjøremål! Kanskje du skal hjelpe partneren din?</div>
				{/if}
			</div>
			<div slot="bottom">
				<NewTaskDropdown />
			</div>
		</TaskBox>

		<div>
			<div class="header">
				<h2>Fullførte</h2>
				<Button on:click={toggleShow}>
					<Icon {iconName} /></Button
				>
			</div>
			{#if showComplete}
				{#each $list as task}
					{#if task.complete}
						<div transition:fly={{ x: -500, duration: 200 }} class="center">
							<ListEntry bind:task />
							<Trash taskSlug={task.slug || ''} />
						</div>
					{/if}
				{/each}
				{#if $list.filter((t) => t.complete).length === 0}
					<div class="none">Ingen fullførte gjøremål! Kanskje du skal gjøre noen?</div>
				{/if}
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

		h2 {
			margin-right: var(--ma);
		}

		.header {
			display: flex;
			align-items: center;
			width: 22rem;
		}
		.center {
			display: flex;
			justify-content: center;
			align-items: center;
			overflow-y: auto;
		}
		.none {
			color: var(--text-color);
		}
	}
</style>
